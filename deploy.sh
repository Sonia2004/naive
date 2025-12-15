#!/bin/bash

# Script para preparar el despliegue en Render

echo "🚀 Preparando aplicación para Render..."

# Verificar que Git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git no está instalado. Instálalo primero:"
    echo "   https://git-scm.com/download/"
    exit 1
fi

# Inicializar Git si no existe
if [ ! -d .git ]; then
    echo "📦 Inicializando repositorio Git..."
    git init
    git add .
    git commit -m "Initial commit: SPAM Detector with Django"
    echo "✅ Repositorio Git creado"
else
    echo "✅ Repositorio Git ya existe"
fi

# Mostrar instrucciones
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         📋 PASOS PARA DESPLEGAR EN RENDER                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "1️⃣  Sube tu código a GitHub:"
echo ""
echo "   git remote add origin https://github.com/TU-USUARIO/spam-detector-django.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "2️⃣  Ve a https://render.com"
echo ""
echo "3️⃣  Haz clic en 'New +' → 'Web Service'"
echo ""
echo "4️⃣  Conecta tu repositorio de GitHub"
echo ""
echo "5️⃣  Completa el formulario con:"
echo ""
echo "   Name:           spam-detector-django"
echo "   Environment:    Python 3"
echo "   Build Command:  pip install -r requirements.txt"
echo "   Start Command:  gunicorn spam_detector.wsgi --log-file -"
echo ""
echo "6️⃣  En 'Environment', agrega estas variables:"
echo ""
echo "   DEBUG=False"
echo "   SECRET_KEY=(genera una nueva clave)"
echo "   CSRF_TRUSTED_ORIGINS=https://tu-app.onrender.com"
echo ""
echo "7️⃣  Haz clic en 'Deploy' y espera"
echo ""
echo "✅ ¡Tu aplicación estará disponible en https://tu-app.onrender.com!"
echo ""
