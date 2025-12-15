# 📋 GUÍA COMPLETA: DESPLIEGUE EN RENDER Y USO DE LA API

## 🚀 PARTE 1: DESPLIEGUE EN RENDER

### Opción A: Despliegue Rápido (Recomendado)

#### 1. Crea una cuenta en GitHub

- Ve a https://github.com/signup
- Crea tu cuenta (o usa la existente)
- Verifica tu email

#### 2. Sube el código a GitHub

Ejecuta estos comandos desde el terminal:

```bash
cd /home/sonia/Descargas/spam_detector_django

# Cambiar rama a main
git branch -M main

# Agregar URL remota (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/spam-detector-django.git

# Subir código
git push -u origin main
```

#### 3. Desplegar en Render

1. Ve a https://render.com
2. Haz clic en **"Sign up"** (o "Sign in" si tienes cuenta)
3. Selecciona **"GitHub"** para conectar
4. Autoriza Render para acceder a tus repositorios
5. Haz clic en **"New +"** → **"Web Service"**
6. Busca **"spam-detector-django"** en tus repositorios
7. Haz clic en **"Connect"**

#### 4. Configurar el despliegue

Completa los campos con:

```
Name:                    spam-detector-django
Environment:             Python 3
Branch:                  main
Build Command:           pip install -r requirements.txt
Start Command:           gunicorn spam_detector.wsgi --log-file -
```

Deja los demás campos por defecto.

#### 5. Agregar variables de entorno

1. En la sección **"Environment Variables"**, haz clic en **"Add Environment Variable"**
2. Agrega estas variables:

```
DEBUG                    False
SECRET_KEY               (genera una: https://djecrety.ir/)
CSRF_TRUSTED_ORIGINS     https://tu-app-name.onrender.com
```

**Nota**: Reemplaza `tu-app-name` con el nombre que elegiste en el paso 4.

#### 6. Iniciar el despliegue

1. Haz clic en **"Deploy"**
2. Espera 5-10 minutos (Render instalará dependencias)
3. Verás **"Your service is live"** cuando esté listo

#### 7. ¡Accede a tu aplicación!

Una vez desplegada, tu app estará disponible en:

```
https://spam-detector-django-xxxxx.onrender.com
```

---

## 🔌 PARTE 2: USAR LA API

### Endpoints disponibles

Tu aplicación tiene una **API REST** completamente funcional:

#### A) Verificar si el modelo está entrenado

```bash
curl -X GET https://tu-app.onrender.com/model-info/
```

#### B) Predecir si un email es SPAM (API REST)

```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Subject: ¡GANA DINERO AHORA!\n\nHaz clic aquí para ganar $1000"}'
```

**Respuesta exitosa:**
```json
{
  "is_spam": true,
  "label": "spam",
  "spam_probability": 0.95,
  "ham_probability": 0.05
}
```

---

## 📝 EJEMPLOS DE USO

### Ejemplo 1: Email SPAM

```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "email_content": "Subject: ¡OFERTA ESPECIAL! 50% descuento\n\nLLAMA AHORA: 1-800-DINERO. ¡¡¡GANA DINERO RÁPIDO!!!"
  }'
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

### Ejemplo 2: Email Legítimo

```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "email_content": "Subject: Reunión de equipo mañana\n\nHola, la reunión será mañana a las 10 AM en la sala de conferencias."
  }'
```

**Respuesta:**
```json
{
  "is_spam": false,
  "label": "ham",
  "spam_probability": 0.02,
  "ham_probability": 0.98
}
```

---

## 🔧 USAR LA API CON PYTHON

```python
import requests
import json

# URL de tu API
API_URL = "https://tu-app.onrender.com/api/predict/"

# Email a analizar
email_content = """Subject: ¡Gana dinero ahora!

Haz clic aquí para ganar $1000 fácilmente."""

# Hacer la petición
response = requests.post(
    API_URL,
    json={"email_content": email_content},
    headers={"Content-Type": "application/json"}
)

# Procesar la respuesta
if response.status_code == 200:
    result = response.json()
    print(f"Es SPAM: {result['is_spam']}")
    print(f"Confianza SPAM: {result['spam_probability']:.2%}")
    print(f"Confianza Legítimo: {result['ham_probability']:.2%}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

---

## 🔧 USAR LA API CON JavaScript

```javascript
const API_URL = "https://tu-app.onrender.com/api/predict/";

const emailContent = `Subject: Reunión importante

La reunión será mañana a las 10 AM.`;

fetch(API_URL, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        email_content: emailContent
    })
})
.then(response => response.json())
.then(data => {
    console.log("Es SPAM:", data.is_spam);
    console.log("Confianza:", Math.max(data.spam_probability, data.ham_probability).toFixed(2));
    console.log("Respuesta completa:", data);
})
.catch(error => console.error("Error:", error));
```

---

## 🔧 USAR LA API CON cURL (Comando Terminal)

### Email SPAM:
```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content":"Subject: ¡GANA DINERO RÁPIDO!\n\nClickea aquí para ganar $10000 sin hacer nada"}'
```

### Email Legítimo:
```bash
curl -X POST https://tu-app.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content":"Subject: Confirmación de tu pedido\n\nTu pedido #12345 ha sido procesado"}'
```

---

## 📊 ACCEDER A LA INTERFAZ WEB

Además de la API, tu aplicación tiene una interfaz web:

### Página Principal (Analizador)
```
https://tu-app.onrender.com/
```

- Modo simple: Ingresa asunto + contenido
- Modo raw: Pegua email completo con headers
- Haz clic en "Analizar Email"

### Historial de Análisis
```
https://tu-app.onrender.com/history/
```

- Ver todos los emails analizados
- Estadísticas de SPAM vs legítimos
- Búsqueda y filtrado

### Información Técnica
```
https://tu-app.onrender.com/model-info/
```

- Detalles del algoritmo Naive Bayes
- Pipeline de procesamiento
- Información del modelo

### Panel de Administración
```
https://tu-app.onrender.com/admin/
```

- Usuario: `admin`
- Contraseña: (la que creaste)
- Gestiona registros, usuarios, etc.

---

## 🆘 TROUBLESHOOTING

### "502 Bad Gateway"
- La app se está iniciando, espera 2-3 minutos
- Verifica que no hay errores en el log de Render

### "Internal Server Error"
- Revisa los logs en Render Dashboard
- Asegúrate de que el SECRET_KEY esté configurado

### "Model not trained"
- El modelo se entrena automáticamente al desplegar
- Espera a que termine el despliegue

### "CSRF verification failed"
- Configura CSRF_TRUSTED_ORIGINS correctamente
- Reemplaza `tu-app` con tu nombre real de Render

---

## 📈 INTEGRAR CON OTROS SERVICIOS

### Integraciones posibles

1. **Con Gmail API**: Analizar emails automáticamente
2. **Con Slack**: Notificar si un email es SPAM
3. **Con Zapier**: Automatizar flujos
4. **Con tu sitio web**: Validar emails en registro

### Ejemplo de integración con Slack

```python
import requests

# Analizar email
api_response = requests.post(
    "https://tu-app.onrender.com/api/predict/",
    json={"email_content": email}
)

result = api_response.json()

# Si es SPAM, notificar a Slack
if result['is_spam']:
    slack_message = f"🚫 Email sospechoso detectado\nConfianza: {result['spam_probability']:.1%}"
    
    requests.post(
        "https://hooks.slack.com/services/TU/WEBHOOK/URL",
        json={"text": slack_message}
    )
```

---

## ✅ CHECKLIST: TODO FUNCIONA

- [ ] Aplicación desplegada en Render
- [ ] Puedo acceder a `https://tu-app.onrender.com`
- [ ] La API responde en `/api/predict/`
- [ ] El modelo está entrenado (sin errores)
- [ ] Puedo analizar emails desde la web
- [ ] Puedo hacer peticiones a la API con curl
- [ ] El historial se guarda correctamente

---

## 📞 PRÓXIMOS PASOS

1. **Prueba la API** con diferentes emails
2. **Integra con tus apps** usando los ejemplos
3. **Monitorea** el uso en el dashboard de Render
4. **Personaliza** el modelo con tus datos
5. **Despliega actualizaciones** con `git push`

---

**¡Tu detector de SPAM está en producción!** 🚀

Para más detalles, revisa:
- README.md - Documentación técnica
- DEPLOYMENT.md - Opciones de despliegue
- RENDER_DEPLOYMENT.md - Específico para Render
