#!/usr/bin/env python
"""
Ejemplos de uso de la API del Detector de SPAM
"""

import os
import sys
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spam_detector.settings')
django.setup()

from spam_ml import spam_detector

# ============================================
# EJEMPLOS DE EMAILS PARA TESTING
# ============================================

SPAM_EXAMPLES = [
    "Subject: ¡OFERTA ESPECIAL! 50% descuento\n\nLLAMA AHORA: 1-800-DINERO. ¡¡¡GANA DINERO RÁPIDO!!!",
    "Subject: Tu cuenta fue comprometida\n\nVerifica tu identidad AHORA en este link falso o perderás acceso",
    "Subject: Felicidades! Ganaste el iPhone 15\n\nAlfin ganaste! Reclama tu premio aquí haciendo click",
    "Subject: Heredaste $5 millones\n\nHola, soy un príncipe nigeriano y he heredado una fortuna para ti",
    "Subject: Amplía tu pene en una semana\n\nProducto milagroso. Cientos de clientes satisfechos. Ordena ahora",
    "Subject: Viagra sin receta\n\nEnvío discreto y rápido. Mejora tu desempeño. CLICK AQUÍ AHORA",
    "Subject: URGENTE: Tu banco necesita tu información\n\nConfirma tus datos bancarios en este sitio",
]

HAM_EXAMPLES = [
    "Subject: Reunión de equipo mañana\n\nHola, la reunión será mañana a las 10 AM en la sala de conferencias 3.",
    "Subject: Confirmación de tu pedido\n\nTu pedido #12345 ha sido procesado. Será entregado en 3-5 días.",
    "Subject: Factura del mes de diciembre\n\nAdjunto encontrarás la factura del mes. Por favor revísala.",
    "Subject: Cambios de horario\n\nNuevos horarios de atención: Lunes a viernes de 9 AM a 6 PM",
    "Subject: Reporte de avance del proyecto\n\nEl proyecto avanza según lo planeado. Detalles en el archivo adjunto.",
    "Subject: Invitación a la cena de navidad\n\nTe invitamos a nuestra cena de navidad. RSVP antes del 15 dic",
    "Subject: Confirmación de asistencia\n\nGracias por confirmar tu asistencia. Te esperamos el viernes.",
]


def print_separator(title=""):
    """Imprime un separador con título."""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print(f"\n{'-'*60}\n")


def test_spam_detection():
    """Prueba la detección de SPAM."""
    
    # Verificar que el modelo está entrenado
    if spam_detector.classifier is None:
        print("❌ El modelo no está entrenado.")
        print("Ejecuta: python train_model.py")
        return
    
    print_separator("🧪 PRUEBAS DE DETECCIÓN DE SPAM")
    
    # Pruebas SPAM
    print("🚫 PRUEBAS CON EMAILS SPAM:\n")
    spam_results = []
    for i, email in enumerate(SPAM_EXAMPLES[:3], 1):
        result, _ = spam_detector.predict(email)
        if result:
            is_correct = result['is_spam']
            emoji = "✓" if is_correct else "✗"
            print(f"{emoji} Ejemplo SPAM #{i}")
            print(f"   Predicción: {result['label'].upper()}")
            print(f"   Confianza: {max(result['spam_probability'], result['ham_probability']):.2%}")
            spam_results.append(is_correct)
    
    print_separator()
    
    # Pruebas HAM
    print("✅ PRUEBAS CON EMAILS LEGÍTIMOS:\n")
    ham_results = []
    for i, email in enumerate(HAM_EXAMPLES[:3], 1):
        result, _ = spam_detector.predict(email)
        if result:
            is_correct = not result['is_spam']
            emoji = "✓" if is_correct else "✗"
            print(f"{emoji} Ejemplo HAM #{i}")
            print(f"   Predicción: {result['label'].upper()}")
            print(f"   Confianza: {max(result['spam_probability'], result['ham_probability']):.2%}")
            ham_results.append(is_correct)
    
    # Resumen
    print_separator("📊 RESUMEN DE RESULTADOS")
    
    total_tests = len(spam_results) + len(ham_results)
    correct_spam = sum(spam_results)
    correct_ham = sum(ham_results)
    total_correct = correct_spam + correct_ham
    accuracy = (total_correct / total_tests * 100) if total_tests > 0 else 0
    
    print(f"SPAM detectados correctamente: {correct_spam}/{len(spam_results)}")
    print(f"HAM detectados correctamente: {correct_ham}/{len(ham_results)}")
    print(f"Precisión general: {accuracy:.1f}%")


def interactive_test():
    """Modo interactivo para probar emails."""
    
    if spam_detector.classifier is None:
        print("❌ El modelo no está entrenado.")
        print("Ejecuta: python train_model.py")
        return
    
    print_separator("🔍 MODO INTERACTIVO")
    print("Ingresa emails para analizar (escribe 'salir' para terminar)")
    print_separator()
    
    while True:
        print("\n📧 Opciones:")
        print("1. Ingresar email manualmente")
        print("2. Usar ejemplo de SPAM")
        print("3. Usar ejemplo de HAM")
        print("4. Salir")
        
        choice = input("\nElige una opción (1-4): ").strip()
        
        if choice == "1":
            email = input("\nPega el email (o presiona Enter para cancelar): ").strip()
            if not email:
                continue
        elif choice == "2":
            email = SPAM_EXAMPLES[0]
            print(f"\nUsando ejemplo SPAM:\n{email[:100]}...")
        elif choice == "3":
            email = HAM_EXAMPLES[0]
            print(f"\nUsando ejemplo HAM:\n{email[:100]}...")
        elif choice == "4":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida")
            continue
        
        result, _ = spam_detector.predict(email)
        
        if result:
            print("\n" + "="*60)
            if result['is_spam']:
                print("🚫 CLASIFICACIÓN: SPAM")
            else:
                print("✅ CLASIFICACIÓN: LEGÍTIMO")
            
            print(f"\nProbabilidades:")
            print(f"  SPAM: {result['spam_probability']:.2%}")
            print(f"  Legítimo: {result['ham_probability']:.2%}")
            
            # Visualizar confianza
            confianza = max(result['spam_probability'], result['ham_probability'])
            barras = int(confianza * 20)
            barra_visual = "█" * barras + "░" * (20 - barras)
            print(f"\nConfianza: [{barra_visual}] {confianza:.2%}")
            print("="*60)


def export_predictions(output_file="predictions.json"):
    """Exporta predicciones a JSON."""
    
    if spam_detector.classifier is None:
        print("❌ El modelo no está entrenado.")
        return
    
    print_separator("💾 EXPORTANDO PREDICCIONES")
    
    results = []
    all_examples = SPAM_EXAMPLES + HAM_EXAMPLES
    labels = ['spam'] * len(SPAM_EXAMPLES) + ['ham'] * len(HAM_EXAMPLES)
    
    for email, expected_label in zip(all_examples, labels):
        result, _ = spam_detector.predict(email)
        if result:
            results.append({
                'email': email[:100],
                'expected': expected_label,
                'predicted': result['label'],
                'spam_probability': result['spam_probability'],
                'ham_probability': result['ham_probability'],
                'correct': result['label'] == expected_label
            })
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Predicciones exportadas a {output_file}")


def main():
    """Menú principal."""
    
    while True:
        print("\n" + "="*60)
        print("  🧠 DETECTOR DE SPAM - EJEMPLOS Y PRUEBAS")
        print("="*60)
        print("\nOpciones:")
        print("1. Ejecutar pruebas automáticas")
        print("2. Modo interactivo")
        print("3. Exportar predicciones a JSON")
        print("4. Salir")
        
        choice = input("\nElige una opción (1-4): ").strip()
        
        if choice == "1":
            test_spam_detection()
        elif choice == "2":
            interactive_test()
        elif choice == "3":
            export_predictions()
        elif choice == "4":
            print("\n¡Gracias por usar el Detector de SPAM! 👋\n")
            break
        else:
            print("❌ Opción no válida")


if __name__ == '__main__':
    main()
