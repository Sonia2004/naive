# Detector de SPAM Django - Quick Start

## ⚡ Inicio Rápido (5 minutos)

### Opción 1: Script automático
```bash
chmod +x setup.sh
./setup.sh
python manage.py runserver
```

### Opción 2: Pasos manuales

**1. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**2. Configurar base de datos**
```bash
python manage.py migrate
```

**3. Entrenar modelo**
```bash
python train_model.py
```

**4. Crear usuario admin** (opcional)
```bash
python manage.py createsuperuser
```

**5. Ejecutar servidor**
```bash
python manage.py runserver
```

## 🌐 Acceder a la aplicación

- **Aplicación Web**: http://localhost:8000
- **Panel Admin**: http://localhost:8000/admin

## 📝 Ejemplo de uso

### 1. Página principal
- Elige entre "Modo Simple" o "Modo Raw"
- Ingresa o pega el contenido del email
- Click en "Analizar Email"

### 2. Ver historial
- Accede a http://localhost:8000/history/
- Visualiza todos los emails analizados
- Ve estadísticas de SPAM vs legítimos

### 3. Información del modelo
- Ve a http://localhost:8000/model-info/
- Aprende sobre Naive Bayes
- Entiende el pipeline de procesamiento

## 🔌 API REST

**Predecir si un email es SPAM:**
```bash
curl -X POST http://localhost:8000/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Subject: ¡Gana dinero ahora!\n\nHaz click aquí"}'
```

**Respuesta:**
```json
{
  "is_spam": true,
  "label": "spam",
  "spam_probability": 0.98,
  "ham_probability": 0.02
}
```

## 🛠️ Personalizar modelo

**Editar datos de entrenamiento**
- Abre `train_model.py`
- Modifica listas `TRAIN_EMAILS` y `TRAIN_LABELS`
- Ejecuta `python train_model.py` nuevamente

## 📊 Ver resultados en admin

1. Accede a http://localhost:8000/admin/
2. Usuario: (el que creaste)
3. Contraseña: (la que estableciste)
4. Navega a "Email Check Records"
5. Visualiza estadísticas de predicciones

## ⚙️ Cambiar puerto

```bash
python manage.py runserver 8001
```

## 🐛 Solucionar problemas

**Error: Port 8000 already in use**
```bash
python manage.py runserver 8001
```

**Error: No module named 'nltk'**
```bash
pip install nltk
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

**Base de datos corrupta**
```bash
rm db.sqlite3
python manage.py migrate
python train_model.py
```

## 📚 Próximos pasos

1. Lee el `README.md` para documentación completa
2. Explora el código en `spam_ml.py`
3. Personaliza los templates HTML en `detector/templates/`
4. Entrena con tus propios datos
5. Integra la API en tus aplicaciones

## 💡 Tips

- El modelo se entrena con datos de ejemplo en `train_model.py`
- Los emails analizados se guardan en la base de datos
- Puedes ver admin en `/admin` para gestionar datos
- La API REST permite integración con otras apps

---

¡Ya puedes detectar SPAM! 🚀
