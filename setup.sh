#!/bin/bash

# Script de inicio rápido para el Detector de SPAM

echo "========================================"
echo "🔧 Detector de SPAM - Setup Rápido"
echo "========================================"
echo ""

# 1. Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# 2. Migraciones de base de datos
echo ""
echo "🗄️  Aplicando migraciones..."
python manage.py migrate

# 3. Entrenar modelo
echo ""
echo "🧠 Entrenando modelo inicial..."
python train_model.py

# 4. Crear superusuario
echo ""
echo "👤 Creando superusuario..."
python manage.py createsuperuser

# 5. Información final
echo ""
echo "========================================"
echo "✅ ¡Instalación completada!"
echo "========================================"
echo ""
echo "Para iniciar la aplicación, ejecuta:"
echo "  python manage.py runserver"
echo ""
echo "Luego accede a:"
echo "  Web: http://localhost:8000"
echo "  Admin: http://localhost:8000/admin"
echo ""
