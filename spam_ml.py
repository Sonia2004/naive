import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spam_detector.settings")
django.setup()

import string
import nltk
import email
from html.parser import HTMLParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import pickle
import json

# Descargar recursos NLTK si es necesario
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


class MLStripper(HTMLParser):
    """Clase para eliminar tags HTML del contenido de emails."""

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return "".join(self.fed)


def strip_tags(html):
    """Elimina los tags HTML de un texto."""
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class EmailParser:
    """Parser para procesar emails y extraer características."""

    def __init__(self):
        self.stemmer = nltk.PorterStemmer()
        self.stopwords = set(nltk.corpus.stopwords.words("english"))
        self.punctuation = list(string.punctuation)

    def parse_text(self, text):
        """Parse y preprocesa un texto de email."""
        if text is None:
            return []

        # Eliminar puntuación
        for c in self.punctuation:
            text = text.replace(c, "")

        # Reemplazar caracteres especiales
        text = text.replace("\t", " ")
        text = text.replace("\n", " ")

        # Tokenizar
        tokens = list(filter(None, text.split(" ")))

        # Stemming y eliminar stopwords
        return [
            self.stemmer.stem(w.lower())
            for w in tokens
            if w.lower() not in self.stopwords
        ]

    def parse_email(self, email_content):
        """Parse un email completo."""
        try:
            msg = email.message_from_string(email_content)

            # Extraer subject
            subject = self.parse_text(msg["Subject"]) if msg["Subject"] else []

            # Extraer body
            payload = msg.get_payload()
            content_type = msg.get_content_type()
            body = self._get_email_body(payload, content_type)

            # Combinar subject y body
            all_tokens = subject + body
            return " ".join(all_tokens)
        except Exception as e:
            print(f"Error parsing email: {e}")
            return ""

    def _get_email_body(self, payload, content_type):
        """Extrae el cuerpo del email."""
        body = []

        if isinstance(payload, str):
            if content_type == "text/plain":
                body = self.parse_text(payload)
            elif content_type == "text/html":
                body = self.parse_text(strip_tags(payload))
        elif isinstance(payload, list):
            for p in payload:
                body += self._get_email_body(p.get_payload(), p.get_content_type())

        return body


class SpamDetector:
    """Detector de SPAM usando Naive Bayes."""

    def __init__(self):
        self.vectorizer = None
        self.classifier = None
        self.parser = EmailParser()
        self.model_path = "models/spam_model.pkl"
        self.vectorizer_path = "models/vectorizer.pkl"
        self._load_model()

    def _load_model(self):
        """Carga el modelo entrenado si existe."""
        try:
            with open(self.vectorizer_path, "rb") as f:
                self.vectorizer = pickle.load(f)
            with open(self.model_path, "rb") as f:
                self.classifier = pickle.load(f)
        except FileNotFoundError:
            # Si no existe, crear uno nuevo vacío
            pass

    def train(self, emails, labels):
        """Entrena el modelo con nuevos datos."""
        # Procesar emails
        processed_emails = [self.parser.parse_email(email) for email in emails]

        # Vectorizar
        self.vectorizer = CountVectorizer(max_features=5000)
        X = self.vectorizer.fit_transform(processed_emails)

        # Entrenar
        self.classifier = BernoulliNB(alpha=1.0e-10)
        self.classifier.fit(X, labels)

        # Guardar modelo
        self._save_model()

    def predict(self, email_content):
        """Predice si un email es SPAM o no."""
        if self.classifier is None or self.vectorizer is None:
            return None, None

        # Procesar email
        processed = self.parser.parse_email(email_content)

        # Vectorizar
        X = self.vectorizer.transform([processed])

        # Predecir
        prediction = self.classifier.predict(X)[0]
        probability = self.classifier.predict_proba(X)[0]

        result = {
            "is_spam": prediction == "spam",
            "label": prediction,
            "spam_probability": float(probability[1]) if len(probability) > 1 else 0.0,
            "ham_probability": float(probability[0]) if len(probability) > 0 else 1.0,
        }

        return result, None

    def _save_model(self):
        """Guarda el modelo entrenado."""
        import os

        os.makedirs("models", exist_ok=True)

        with open(self.vectorizer_path, "wb") as f:
            pickle.dump(self.vectorizer, f)
        with open(self.model_path, "wb") as f:
            pickle.dump(self.classifier, f)

    def get_feature_names(self):
        """Obtiene los nombres de las características del vectorizador."""
        if self.vectorizer is None:
            return []
        try:
            return list(self.vectorizer.get_feature_names_out())
        except AttributeError:
            return list(self.vectorizer.get_feature_names())


# Crear instancia global del detector
spam_detector = SpamDetector()
