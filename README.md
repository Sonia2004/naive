# 📧 Detector de SPAM con Django y Machine Learning

Una aplicación web completa para detectar emails de SPAM utilizando Django y el algoritmo **Naive Bayes**.

## 🎯 Características

- **Detector de SPAM basado en ML**: Utiliza Naive Bayes para clasificar emails
- **Interfaz web intuitiva**: Interfaz moderna con Bootstrap 5
- **Dos modos de entrada**: 
  - Modo simple: Asunto + Contenido
  - Modo Raw: Email completo con headers
- **Historial de análisis**: Guarda todos los emails analizados
- **Estadísticas**: Visualiza información sobre predicciones
- **API REST**: Endpoint para integrar el detector con otras aplicaciones
- **Información del modelo**: Detalles técnicos sobre el algoritmo

## 🛠️ Requisitos

- Python 3.8+
- Django 4.2+
- scikit-learn
- nltk

## 📦 Instalación

### 1. Clonar o descargar el proyecto
```bash
cd /home/sonia/Descargas/spam_detector_django
```

### 2. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Entrenar el modelo inicial (opcional)
```bash
python train_model.py
```

Este script entrena el modelo con datos de ejemplo. Puedes modificar el archivo `train_model.py` para usar tus propios datos.

### 6. Crear superusuario (para admin)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

Accede a la aplicación en: **http://localhost:8000**

## 🎮 Cómo usar

### Analizador Web
1. Ve a http://localhost:8000/
2. Elige entre dos opciones:
   - **Modo Simple**: Ingresa el asunto y contenido del email
   - **Modo Raw**: Pegua el email completo con headers
3. Haz click en "Analizar Email"
4. Obtendrás el resultado con probabilidades

### Historial
- Accede a `/history/` para ver todos los emails analizados
- Visualiza estadísticas y distribución de SPAM vs legítimos
- Expande cada registro para ver el contenido completo

### Información del Modelo
- Ve a `/model-info/` para detalles técnicos
- Aprende sobre el algoritmo Naive Bayes
- Entiende el pipeline de procesamiento

### API REST
```bash
curl -X POST http://localhost:8000/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Tu contenido aquí"}'
```

Respuesta:
```json
{
  "is_spam": true,
  "label": "spam",
  "spam_probability": 0.95,
  "ham_probability": 0.05
}
```

## 🧠 Algoritmo Naive Bayes

El algoritmo Naive Bayes es un método de clasificación probabilístico basado en el teorema de Bayes con la suposición de independencia entre características.

### Por qué Naive Bayes para SPAM detection?

1. **Velocidad**: Entrenamiento y predicción muy rápidos
2. **Eficiencia**: Requiere menos memoria
3. **Probabilidades**: Proporciona valores de confianza
4. **Simplicidad**: Fácil de entender e interpretar
5. **Escalabilidad**: Funciona bien con conjuntos grandes

### Pipeline de Procesamiento

1. **Lectura de Email**: Carga contenido (raw o estructurado)
2. **Limpieza HTML**: Extrae texto sin tags
3. **Tokenización**: Divide en palabras
4. **Stemming**: Reduce a raíz (ej: 'correos' → 'corr')
5. **Stopwords**: Elimina palabras comunes
6. **Vectorización**: Convierte a matriz numérica
7. **Clasificación**: Predice SPAM o legítimo

## 📁 Estructura del Proyecto

```
spam_detector_django/
├── spam_detector/          # Configuración principal
│   ├── settings.py        # Configuración Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py
├── detector/              # Aplicación principal
│   ├── migrations/        # Migraciones BD
│   ├── templates/
│   │   └── detector/
│   │       ├── base.html          # Template base
│   │       ├── index.html         # Página principal
│   │       ├── result.html        # Resultados
│   │       ├── history.html       # Historial
│   │       └── model_info.html    # Info modelo
│   ├── models.py          # Modelos de BD
│   ├── views.py           # Vistas Django
│   ├── forms.py           # Formularios
│   └── urls.py            # URLs de app
├── spam_ml.py             # Lógica ML (Naive Bayes)
├── train_model.py         # Script de entrenamiento
├── manage.py              # CLI Django
├── requirements.txt       # Dependencias
└── db.sqlite3            # Base de datos (creada automáticamente)
```

## 🔧 Configuración

### Personalizar umbral de SPAM
Edita `spam_ml.py` en la clase `SpamDetector`:
```python
# Cambiar sensibilidad del modelo
self.classifier = BernoulliNB(alpha=1.0e-10)  # Ajusta alpha
```

### Entrenar con tus propios datos
Crea un script similar a `train_model.py`:
```python
from spam_ml import spam_detector

emails = [...]  # Tus emails
labels = [...]  # 'spam' o 'ham'

spam_detector.train(emails, labels)
```

## 📊 Base de Datos

La aplicación usa SQLite (por defecto) para guardar:
- Emails analizados
- Predicciones
- Timestamps

Para cambiar a PostgreSQL, modifica `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spam_detector',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🔐 Seguridad

Para producción:
1. Cambia `DEBUG = False` en `settings.py`
2. Genera una nueva `SECRET_KEY`
3. Configura `ALLOWED_HOSTS`
4. Usa HTTPS
5. Guarda contraseñas en variables de entorno

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['tudominio.com']
```

## 🧪 Testing

Ejecuta las pruebas:
```bash
python manage.py test detector
```

## 📈 Mejoras Futuras

- [ ] Soporte para múltiples idiomas
- [ ] Integración con proveedores de email (Gmail, Outlook)
- [ ] Dashboard de análisis avanzado
- [ ] Exportar reportes (PDF, CSV)
- [ ] Modelo actualizable online
- [ ] Detección de phishing
- [ ] Análisis de adjuntos
- [ ] Machine Learning avanzado (SVM, Random Forest)

## 🐛 Troubleshooting

### Error: "Model not trained"
Ejecuta `python train_model.py` para entrenar el modelo

### Error: "No module named 'nltk'"
```bash
pip install nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Puerto 8000 ya en uso
```bash
python manage.py runserver 8001
```

## 📚 Recursos

- [Documentación Django](https://docs.djangoproject.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Naive Bayes Theory](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Creado como proyecto educativo de Machine Learning con Django.

---

**¿Preguntas?** Revisa los templates HTML para entender la interfaz o modifica `spam_ml.py` para ajustar el modelo.

¡Disfruta detectando SPAM! 🚀
# naive
