# 🚀 Despliegue en Render

## Pasos para desplegar en Render

### 1. Preparar el repositorio

Primero, asegúrate de que todos los archivos están listos:

```bash
cd /home/sonia/Descargas/spam_detector_django
```

### 2. Crear un repositorio Git

```bash
git init
git add .
git commit -m "Initial commit: SPAM Detector with Django"
```

### 3. Subir a GitHub

- Crea una cuenta en GitHub (si no la tienes)
- Crea un nuevo repositorio llamado `spam-detector-django`
- Sube tu código:

```bash
git remote add origin https://github.com/tu-usuario/spam-detector-django.git
git branch -M main
git push -u origin main
```

### 4. Crear la aplicación en Render

1. Ve a https://render.com
2. Haz clic en "New +"
3. Selecciona "Web Service"
4. Conecta tu repositorio de GitHub
5. Completa el formulario:

**Configuración**:
```
Name: spam-detector-django
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn spam_detector.wsgi --log-file -
```

### 5. Configurar variables de entorno

En Render, ve a "Environment" y agrega:

```
DEBUG=False
SECRET_KEY=tu-clave-secreta-aqui
CSRF_TRUSTED_ORIGINS=https://tu-app.onrender.com
```

### 6. Desplegar

Haz clic en "Deploy" y espera a que se complete la instalación.

---

## 📍 Tu aplicación estará disponible en:

```
https://tu-app.onrender.com
```

---

## 🔌 API REST disponible en:

```
https://tu-app.onrender.com/api/predict/
```

### Uso de la API:

```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Tu contenido de email aquí"}'
```

---

## ✅ Después del despliegue

1. Visita tu aplicación
2. La BD se creará automáticamente
3. El modelo se entrenará automáticamente
4. ¡Listo para usar!

---

## 🆘 Troubleshooting

**Error: "No module named 'nltk'"**
- Render descargará las dependencias automáticamente

**Error: "Model not trained"**
- Se entrena automáticamente en el release

**Puerto incorrecto**
- Render asigna puertos automáticamente, no necesitas configurar nada

---

**¡Tu aplicación está lista para producción!** 🎉
