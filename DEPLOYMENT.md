# 🚀 INSTALACIÓN Y DESPLIEGUE

## ⚡ Instalación Rápida (Windows, Mac, Linux)

### Prerequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

### Paso 1: Descargar el proyecto
```bash
cd /home/sonia/Descargas/spam_detector_django
```

### Paso 2: Crear entorno virtual (RECOMENDADO)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar base de datos
```bash
python manage.py migrate
```

### Paso 5: Entrenar modelo
```bash
python train_model.py
```

### Paso 6: Crear usuario admin (opcional)
```bash
python manage.py createsuperuser
```

### Paso 7: Ejecutar servidor
```bash
python manage.py runserver
```

**Accede a**: http://localhost:8000

---

## 🐳 Instalación con Docker

### Crear Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
RUN python train_model.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Ejecutar con Docker
```bash
docker build -t spam-detector .
docker run -p 8000:8000 spam-detector
```

---

## ☁️ Desplegar en Heroku

### 1. Crear Procfile
```
web: gunicorn spam_detector.wsgi
release: python manage.py migrate
```

### 2. Crear runtime.txt
```
python-3.11.0
```

### 3. Instalar Heroku CLI
```bash
# https://devcenter.heroku.com/articles/heroku-cli
heroku login
```

### 4. Desplegar
```bash
heroku create nombre-tu-app
heroku config:set SECRET_KEY="tu-clave-secreta"
git push heroku main
```

---

## 🌐 Desplegar en PythonAnywhere

### 1. Registrarse
Ir a https://www.pythonanywhere.com/

### 2. Crear cuenta
- Username: tu nombre
- Email: tu email
- Password: tu contraseña

### 3. Subir archivos
```bash
# Desde tu terminal local
scp -r spam_detector_django/* tu_usuario@ssh.pythonanywhere.com:~/mysite/
```

### 4. Configurar en PythonAnywhere
- Web → Add a new web app
- Python 3.10
- Django
- Configurar archivos de settings

---

## 🚀 Desplegar en AWS

### 1. Crear instancia EC2
```bash
# SSH a tu instancia
ssh -i tu-key.pem ec2-user@tu-ip-publica

# Instalar Python
sudo yum update -y
sudo yum install python3 python3-pip -y
```

### 2. Clonar proyecto
```bash
git clone tu-repo
cd spam_detector_django
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
pip install gunicorn
```

### 4. Configurar con Nginx
```bash
sudo yum install nginx -y
sudo systemctl start nginx
```

Crear `/etc/nginx/sites-available/spam_detector`:
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 5. Ejecutar con Gunicorn
```bash
gunicorn spam_detector.wsgi:application --bind 0.0.0.0:8000
```

---

## 🔒 Producción - Checklist

### Django Settings
- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` en variable de entorno
- [ ] `ALLOWED_HOSTS` configurado
- [ ] `SECURE_SSL_REDIRECT = True`
- [ ] `SESSION_COOKIE_SECURE = True`
- [ ] `CSRF_COOKIE_SECURE = True`

### Server
- [ ] HTTPS/SSL certificado
- [ ] Firewall configurado
- [ ] Backups automáticos de BD
- [ ] Logs monitoreados
- [ ] Email configurado

### Security
- [ ] Cambiar SECRET_KEY
- [ ] Usar variables de entorno
- [ ] Contraseñas fuertes para admin
- [ ] CORS configurado
- [ ] Rate limiting activado

---

## 📊 Monitoreo

### Logs en Producción
```bash
# Ver logs en tiempo real
tail -f logs/error.log

# Buscar errores específicos
grep "ERROR" logs/error.log
```

### Métricas
```bash
# Ver uso de CPU/RAM
top

# Procesos Python
ps aux | grep python

# Puerto en uso
netstat -tlnp | grep :8000
```

---

## 🔄 Actualizaciones

### Actualizar código
```bash
git pull origin main
```

### Instalar nuevas dependencias
```bash
pip install -r requirements.txt
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Reentrenar modelo
```bash
python train_model.py
```

### Reiniciar servidor
```bash
# Si usas Systemd
sudo systemctl restart spam-detector

# Si usas Gunicorn
pkill -f gunicorn
gunicorn spam_detector.wsgi:application --bind 0.0.0.0:8000
```

---

## 🆘 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'django'"
```bash
pip install -r requirements.txt
```

### Error: "Port 8000 is already in use"
```bash
# Encuentra qué proceso usa el puerto
lsof -i :8000

# O usa otro puerto
python manage.py runserver 8001
```

### Error: "database locked"
```bash
# Elimina y recrea la BD
rm db.sqlite3
python manage.py migrate
python train_model.py
```

### Error: "NLTK data not found"
```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

---

## 📞 Soporte

- Documentación: Ver `README.md`
- Inicio rápido: Ver `QUICKSTART.md`
- Resumen: Ver `RESUMEN.md`

---

**¡Tu aplicación de Detector de SPAM está lista para producción!** 🎉
