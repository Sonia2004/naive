# 🚀 DESPLEGAR EN RENDER - PASOS EXACTOS

## ✅ CÓDIGO LISTO EN GIT

Tu código está listo. Ahora sigue estos pasos:

---

## PASO 1: Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `spam-detector-django`
3. Descripción: `SPAM Detector with Django and Naive Bayes`
4. **Importante**: Selecciona "Public" (Render necesita verlo)
5. Haz clic en "Create repository"

---

## PASO 2: Subir tu código a GitHub

En tu terminal, ejecuta estos comandos:

```bash
cd /home/sonia/Descargas/spam_detector_django

# Cambiar nombre de rama a main
git branch -M main

# Agregar tu repositorio de GitHub (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/spam-detector-django.git

# Subir el código
git push -u origin main
```

**Nota**: Te pedirá tu usuario y contraseña de GitHub (o token si tienes 2FA)

---

## PASO 3: Crear cuenta en Render (GRATIS)

1. Ve a https://render.com
2. Haz clic en "Sign Up"
3. Selecciona "Continue with GitHub"
4. Autoriza Render para acceder a tus repositorios

---

## PASO 4: Crear Web Service en Render

1. En tu Dashboard de Render, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. Busca tu repositorio **"spam-detector-django"**
4. Si no aparece, haz clic en "Configure account" para dar permisos

---

## PASO 5: Configurar el despliegue

Completa el formulario con exactamente esto:

```
Name:                    spam-detector-django
Environment:             Python 3
Region:                  (dejar por defecto)
Branch:                  main
Build Command:           pip install -r requirements.txt
Start Command:           gunicorn spam_detector.wsgi --log-file -
Instance Type:           Free
```

---

## PASO 6: Agregar variables de entorno

1. En el mismo formulario, busca **"Advanced"** ↓
2. Haz clic en **"Add Environment Variable"**
3. Agrega estas variables:

```
DEBUG                    False

SECRET_KEY               (GENERA UNA NUEVA en https://djecrety.ir/)
                         Copia la clave generada aquí

CSRF_TRUSTED_ORIGINS     https://spam-detector-django.onrender.com
```

**Nota**: En la variable `CSRF_TRUSTED_ORIGINS`, asegúrate de usar el nombre correcto que Render te asignará.

---

## PASO 7: Iniciar despliegue

1. Haz clic en **"Deploy Web Service"**
2. ⏳ Espera 5-10 minutos
3. Verás los logs de instalación en tiempo real
4. Cuando diga **"Your service is live"**, ¡está listo!

---

## 🎉 ¡TU APP ESTÁ DESPLEGADA!

Una vez en vivo, accederás en:

```
https://spam-detector-django.onrender.com/
```

---

## 🔌 USA LA API

Tu API REST estará disponible en:

```
POST https://spam-detector-django.onrender.com/api/predict/
```

### Ejemplo:

```bash
curl -X POST https://spam-detector-django.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"email_content": "Subject: ¡GANA DINERO RÁPIDO!\n\nHaz clic aquí para ganar"}'
```

### Respuesta:

```json
{
  "is_spam": true,
  "label": "spam",
  "spam_probability": 0.95,
  "ham_probability": 0.05
}
```

---

## 📍 LINKS DE TU APLICACIÓN

Una vez desplegada, podrás acceder a:

- **Web App**: https://spam-detector-django.onrender.com/
- **Analizador**: https://spam-detector-django.onrender.com/
- **Historial**: https://spam-detector-django.onrender.com/history/
- **Info Modelo**: https://spam-detector-django.onrender.com/model-info/
- **API**: https://spam-detector-django.onrender.com/api/predict/
- **Admin**: https://spam-detector-django.onrender.com/admin/

---

## ❌ TROUBLESHOOTING

### "502 Bad Gateway"
- La app se está iniciando, espera 2-3 minutos
- Verifica los logs en Render

### "Build failed"
- Verifica que `requirements.txt` tenga todas las dependencias
- Revisa que `Procfile` existe

### "Model not trained"
- El modelo se entrena automáticamente
- Espera a que termine el despliegue

### "CSRF verification failed"
- Verifica que `CSRF_TRUSTED_ORIGINS` sea exacto
- Incluye `https://` y el dominio correcto

---

## 📊 VER LOGS EN RENDER

Si algo falla:
1. Ve a tu aplicación en Render
2. Haz clic en **"Logs"**
3. Verás qué salió mal
4. Arregla el problema y hace `git push` (redesplegará automáticamente)

---

## 🔄 ACTUALIZAR CÓDIGO

Para hacer cambios y redeplegar:

```bash
cd /home/sonia/Descargas/spam_detector_django

# Haz tus cambios, luego:
git add .
git commit -m "Tu mensaje de cambio"
git push origin main

# Render redesplegará automáticamente
```

---

## ✅ CHECKLIST

- [ ] Código en GitHub
- [ ] Cuenta en Render creada
- [ ] Web Service creado
- [ ] Variables de entorno configuradas
- [ ] Despliegue iniciado
- [ ] Espera a "Your service is live"
- [ ] Accede a la URL y verifica
- [ ] Prueba la API con curl

---

## 🎁 BONUS: Tu aplicación es

✅ **Gratis** (Tier free de Render)
✅ **Escalable** (Puedes mejorar luego)
✅ **Automático** (Se redeploy con cada git push)
✅ **Seguro** (HTTPS automático)
✅ **Funcional** (Listo para producción)

---

## ¡LISTO!

Sigue estos pasos y tu aplicación estará en vivo en 10 minutos.

Si necesitas ayuda, revisa:
- `00_LEER_PRIMERO.txt`
- `API_GUIDE.md`
- `README.md`

¡Disfruta tu detector de SPAM en producción! 🚀
