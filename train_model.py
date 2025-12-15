#!/usr/bin/env python
"""
Script para entrenar el modelo de Naive Bayes con datos de ejemplo.
Utiliza emails de prueba para demostración.
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spam_detector.settings')
django.setup()

from spam_ml import spam_detector

# Datos de ejemplo para entrenamiento
TRAIN_EMAILS = [
    # SPAM ejemplos
    "Subject: ¡Gana dinero rápido!\n\nClick aquí para ganar dinero en casa. Oferta limitada!",
    "Subject: URGENTE: Herencia de millones\n\nHe heredado $5 millones de un tío lejano...",
    "Subject: Viagra gratis\n\nObtén Viagra sin receta, envío rápido y discreto",
    "Subject: Tu cuenta fue comprometida\n\nVerifica tu identidad ahora o perderás acceso a tu cuenta",
    "Subject: Felicidades! Ganaste un iPhone\n\nHas ganado un iPhone 15 Pro. Reclama tu premio aquí",
    "Subject: Amplía tu pene 5cm en una semana\n\nProducto comprobado científicamente",
    "Subject: 50% descuento en todo\n\n¡¡¡COMPRA AHORA!!! Oferta válida solo hoy",
    "Subject: Préstamo aprobado\n\nSin trámites, sin comprobantes. Dinero en 24 horas",
    
    # HAM ejemplos
    "Subject: Reunión de equipo mañana\n\nHola, la reunión de equipo será mañana a las 10 AM en la sala de conferencias.",
    "Subject: Confirmación de pedido #12345\n\nTu pedido ha sido procesado. Será entregado en 3-5 días hábiles.",
    "Subject: Factura del mes\n\nAdjunto encontrarás la factura del mes. Por favor, revísala y confirma.",
    "Subject: Cambios en el calendario\n\nLos horarios de atención han sido modificados. Ver detalles adjuntos.",
    "Subject: Información sobre el proyecto\n\nComo hablamos, aquí está la información del nuevo proyecto que discutimos.",
    "Subject: Confirmación de asistencia\n\nGracias por confirmar tu asistencia al evento. Nos vemos el viernes.",
    "Subject: Reporte de ventas\n\nEl reporte de ventas del trimestre está disponible. Revisa el archivo adjunto.",
    "Subject: Invitación al evento\n\nEstamos invitándote a nuestra cena de fin de año. RSVP antes del 15 de diciembre.",
]

TRAIN_LABELS = [
    # SPAM
    'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
    # HAM
    'ham', 'ham', 'ham', 'ham', 'ham', 'ham', 'ham', 'ham',
]

def train_model():
    """Entrena el modelo con los datos de ejemplo."""
    print("=" * 60)
    print("Entrenando modelo de Naive Bayes para detección de SPAM")
    print("=" * 60)
    
    print(f"\n📧 Emails de entrenamiento: {len(TRAIN_EMAILS)}")
    print(f"   - SPAM: {TRAIN_LABELS.count('spam')}")
    print(f"   - HAM (legítimos): {TRAIN_LABELS.count('ham')}")
    
    print("\n🔄 Entrenando modelo...")
    spam_detector.train(TRAIN_EMAILS, TRAIN_LABELS)
    
    print("✅ Modelo entrenado exitosamente!")
    print(f"📚 Características en vectorizador: {len(spam_detector.get_feature_names())}")
    
    # Hacer algunas predicciones de prueba
    print("\n" + "=" * 60)
    print("Predicciones de prueba:")
    print("=" * 60)
    
    test_emails = [
        ("Subject: ¡Gana $1000 ahora!\n\nClickea aquí para ganar dinero fácil", 'spam'),
        ("Subject: Reunión mañana\n\nLa reunión será mañana a las 10 AM", 'ham'),
        ("Subject: Oferta especial\n\nTenemos una oferta especial para ti", 'spam'),
    ]
    
    for email, expected in test_emails:
        result, _ = spam_detector.predict(email)
        if result:
            emoji = "🚫" if result['is_spam'] else "✅"
            match = "✓" if (result['label'] == expected) else "✗"
            print(f"\n{emoji} Predicción: {result['label'].upper()}")
            print(f"   Confianza: {max(result['spam_probability'], result['ham_probability']):.2%}")
            print(f"   Esperado: {expected.upper()} {match}")
            print(f"   Email: {email.split(chr(10))[0][:50]}")


if __name__ == '__main__':
    train_model()
