# 📚 ÍNDICE DEL PROYECTO - Detector de SPAM con Django

## 📖 Documentación

### Para empezar
1. **[RESUMEN.md](RESUMEN.md)** - Visión general del proyecto ⭐ LEER PRIMERO
2. **[QUICKSTART.md](QUICKSTART.md)** - Inicio en 5 minutos
3. **[README.md](README.md)** - Documentación completa

### Temas avanzados
4. **[DEPLOYMENT.md](DEPLOYMENT.md)** - Instalación y despliegue en producción
5. **[INSTALL.md](INSTALL.md)** - Guía de instalación detallada

---

## 📁 Estructura de Carpetas

```
spam_detector_django/
│
├── 📚 DOCUMENTACIÓN
│   ├── README.md              ← Documentación completa
│   ├── QUICKSTART.md          ← Inicio rápido
│   ├── RESUMEN.md             ← Resumen del proyecto
│   ├── DEPLOYMENT.md          ← Desplegar en producción
│   └── INDEX.md               ← Este archivo
│
├── ⚙️ CONFIGURACIÓN
│   ├── manage.py              ← CLI Django
│   ├── requirements.txt        ← Dependencias Python
│   ├── .env.example            ← Variables de entorno (ejemplo)
│   ├── .gitignore              ← Archivos a ignorar en Git
│   └── setup.sh                ← Script de instalación automática
│
├── 🧠 MACHINE LEARNING
│   ├── spam_ml.py             ← Lógica de ML (Naive Bayes)
│   ├── train_model.py         ← Entrenar el modelo
│   ├── examples.py            ← Herramienta interactiva de testing
│   └── models/                ← Modelos guardados (generado al entrenar)
│
├── 🎭 APLICACIÓN WEB (Django)
│   ├── spam_detector/         ← Configuración principal
│   │   ├── settings.py        ← Configuración Django
│   │   ├── urls.py            ← URLs principales
│   │   ├── wsgi.py            ← WSGI para producción
│   │   └── asgi.py            ← ASGI para async
│   │
│   └── detector/              ← App principal
│       ├── models.py          ← Modelos de BD
│       ├── views.py           ← Vistas (lógica)
│       ├── urls.py            ← URLs de la app
│       ├── forms.py           ← Formularios
│       ├── admin.py           ← Panel de administración
│       ├── apps.py            ← Configuración de app
│       ├── tests.py           ← Tests unitarios
│       │
│       ├── migrations/        ← Migraciones de BD
│       │   └── __init__.py
│       │
│       └── templates/         ← Templates HTML
│           └── detector/
│               ├── base.html          ← Template base
│               ├── index.html         ← Página principal
│               ├── result.html        ← Página de resultados
│               ├── history.html       ← Historial
│               └── model_info.html    ← Información técnica
│
└── 🗄️ BASE DE DATOS
    └── db.sqlite3            ← BD (generada automáticamente)
```

---

## 🚀 Guías Rápidas

### ¿Por dónde empiezo?
1. Lee `RESUMEN.md` (5 min)
2. Sigue `QUICKSTART.md` para instalar (5 min)
3. Explora la interfaz web (10 min)
4. Lee documentación específica según necesites

### ¿Cómo uso la aplicación?
- Página principal: `http://localhost:8000`
- Historial: `http://localhost:8000/history/`
- Info modelo: `http://localhost:8000/model-info/`
- Admin: `http://localhost:8000/admin/`

### ¿Cómo entreno con mis datos?
1. Edita `train_model.py`
2. Modifica `TRAIN_EMAILS` y `TRAIN_LABELS`
3. Ejecuta `python train_model.py`

### ¿Cómo desplegó en producción?
Revisa `DEPLOYMENT.md` para opciones:
- Heroku (más fácil)
- AWS
- DigitalOcean
- PythonAnywhere
- Docker

---

## 📖 Archivos Principales Explicados

### `spam_ml.py` - Corazón del ML
- **MLStripper**: Elimina tags HTML
- **EmailParser**: Procesa emails
- **SpamDetector**: Modelo Naive Bayes
- **Líneas clave**:
  - 60: Eliminación de stopwords
  - 110: Entrenamiento del modelo
  - 130: Predicción

### `detector/views.py` - Lógica Web
- **index()**: Página principal y formulario
- **history()**: Historial de análisis
- **api_predict()**: API REST
- **model_info()**: Info técnica

### `detector/models.py` - Base de Datos
- **EmailCheckRecord**: Guarda predicciones
  - email_content: Contenido del email
  - prediction: SPAM o HAM
  - confidence: Probabilidad
  - created_at: Timestamp

### `detector/templates/base.html` - Template Base
- Navbar con navegación
- Estilos Bootstrap 5
- Footer

---

## 🔧 Comandos Útiles

### Desarrollo
```bash
python manage.py runserver                # Iniciar servidor
python manage.py migrate                  # Aplicar migraciones
python manage.py createsuperuser          # Crear admin
python manage.py shell                    # Terminal Django
python manage.py test                     # Ejecutar tests
```

### Machine Learning
```bash
python train_model.py                     # Entrenar modelo
python examples.py                        # Herramienta interactiva
```

### Base de Datos
```bash
python manage.py dbshell                  # Shell BD
python manage.py dumpdata > backup.json   # Backup
python manage.py loaddata backup.json     # Restore
```

### Producción
```bash
python manage.py collectstatic            # Recopilar archivos estáticos
python manage.py check --deploy           # Verificar configuración
```

---

## 🧪 Testing

### Ejecutar tests
```bash
python manage.py test detector            # Tests de la app
python manage.py test                     # Todos los tests
```

### Tests disponibles
- `EmailCheckViewTests`: Vistas web
- `EmailCheckRecordTests`: Modelo de BD
- `SpamMLTests`: Lógica de ML

---

## 🔐 Variables de Entorno

Copia `.env.example` a `.env`:
```bash
cp .env.example .env
```

Variables importantes:
- `SECRET_KEY`: Clave secreta Django
- `DEBUG`: True (desarrollo) / False (producción)
- `ALLOWED_HOSTS`: Dominios permitidos

---

## 📊 Tecnologías Utilizadas

### Backend
- **Django 4.2**: Framework web
- **Scikit-learn**: Machine Learning
- **NLTK**: Procesamiento de lenguaje

### Frontend
- **Bootstrap 5**: Framework CSS
- **HTML5**: Estructura
- **CSS3**: Estilos

### BD
- **SQLite**: Desarrollo (por defecto)
- **PostgreSQL**: Producción (opcional)

### Deployment
- **Gunicorn**: Servidor WSGI
- **Nginx**: Reverse proxy
- **Docker**: Containerización

---

## 🎓 Conceptos Clave

### Algoritmo Naive Bayes
- Clasificador probabilístico
- Basado en teorema de Bayes
- Ideal para categorización de texto
- Muy rápido y escalable

### Pipeline ML
```
Email Raw → Limpieza → Tokenización → Stemming → 
Eliminar Stopwords → Vectorización → Clasificación
```

### Vectorización
- Convierte texto a números
- Usa CountVectorizer
- Crea matriz de ocurrencia de palabras

---

## 🐛 Solucionar Problemas

### Problema: "Model not trained"
**Solución**: `python train_model.py`

### Problema: "Module not found"
**Solución**: `pip install -r requirements.txt`

### Problema: Puerto en uso
**Solución**: `python manage.py runserver 8001`

Más en `DEPLOYMENT.md`

---

## 📈 Próximos Pasos

### Aprendizaje
- [ ] Entiende cómo funciona Naive Bayes
- [ ] Modifica los datos de entrenamiento
- [ ] Experimenta con parámetros del modelo
- [ ] Lee el código de `spam_ml.py`

### Desarrollo
- [ ] Agrega nuevas vistas
- [ ] Personaliza templates
- [ ] Integra con tu BD
- [ ] Agrega más modelos ML

### Producción
- [ ] Configura HTTPS
- [ ] Configura variables de entorno
- [ ] Establece backups automáticos
- [ ] Configura monitoreo
- [ ] Despliega en servidor

---

## 🔗 Enlaces Útiles

### Documentación oficial
- [Django](https://www.djangoproject.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Bootstrap 5](https://getbootstrap.com/)

### Recursos ML
- [Naive Bayes Wikipedia](https://es.wikipedia.org/wiki/Clasificador_bayesiano_ingenuo)
- [Scikit-learn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)

---

## 👨‍💻 Créditos

Proyecto educativo de Machine Learning + Django  
Convertido de Jupyter Notebook a aplicación web  
Diciembre 2024

---

## 📞 Ayuda

### ¿Preguntas sobre...?

| Tema | Ver |
|------|-----|
| Cómo empezar | QUICKSTART.md |
| Instalación | DEPLOYMENT.md |
| Algoritmo | README.md > Algoritmo |
| API | README.md > API REST |
| Errores | DEPLOYMENT.md > Troubleshooting |
| Código | Comenta en el código |

---

## 📝 Licencia

MIT License - Libre para usar, modificar y distribuir

---

**Última actualización**: 14 de diciembre de 2024  
**Versión**: 1.0.0  
**Autor**: Proyecto Educativo

🚀 ¡Disfruta detectando SPAM!
