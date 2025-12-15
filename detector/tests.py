from django.test import TestCase, Client
from django.urls import reverse
from detector.models import EmailCheckRecord


class EmailCheckViewTests(TestCase):
    """Pruebas para las vistas del detector."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.client = Client()
    
    def test_index_page_loads(self):
        """Verifica que la página principal carga correctamente."""
        response = self.client.get(reverse('detector:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detector/index.html')
    
    def test_history_page_loads(self):
        """Verifica que la página de historial carga correctamente."""
        response = self.client.get(reverse('detector:history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detector/history.html')
    
    def test_model_info_page_loads(self):
        """Verifica que la página de info del modelo carga correctamente."""
        response = self.client.get(reverse('detector:model_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detector/model_info.html')


class EmailCheckRecordTests(TestCase):
    """Pruebas para el modelo EmailCheckRecord."""
    
    def test_create_record(self):
        """Verifica la creación de un registro."""
        record = EmailCheckRecord.objects.create(
            email_content="Test email content",
            subject="Test Subject",
            prediction='ham',
            confidence=0.95
        )
        
        self.assertEqual(record.prediction, 'ham')
        self.assertEqual(record.confidence, 0.95)
        self.assertEqual(str(record.subject), "Test Subject")
    
    def test_record_ordering(self):
        """Verifica que los registros se ordenan por fecha descendente."""
        record1 = EmailCheckRecord.objects.create(
            email_content="Email 1",
            prediction='spam',
            confidence=0.8
        )
        record2 = EmailCheckRecord.objects.create(
            email_content="Email 2",
            prediction='ham',
            confidence=0.9
        )
        
        records = EmailCheckRecord.objects.all()
        self.assertEqual(records[0].id, record2.id)  # Más reciente primero
        self.assertEqual(records[1].id, record1.id)


class SpamMLTests(TestCase):
    """Pruebas para la lógica de Machine Learning."""
    
    def test_email_parser_basic(self):
        """Verifica el parser de emails."""
        from spam_ml import EmailParser
        
        parser = EmailParser()
        text = "Hello World"
        result = parser.parse_text(text)
        
        # Debería contener palabras procesadas
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
    
    def test_html_stripping(self):
        """Verifica la eliminación de HTML."""
        from spam_ml import strip_tags
        
        html = '<div>Hello <b>World</b></div>'
        result = strip_tags(html)
        
        self.assertEqual(result, 'Hello World')
        self.assertNotIn('<', result)
        self.assertNotIn('>', result)
