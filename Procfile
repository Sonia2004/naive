web: gunicorn spam_detector.wsgi --log-file -
release: python manage.py migrate && python train_model.py
