from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import sys
import os

# Agregar el directorio padre para importar spam_ml
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from spam_ml import spam_detector
from .models import EmailCheckRecord
from .forms import EmailCheckForm


def index(request):
    """Vista principal del detector de SPAM."""
    if request.method == 'POST':
        form = EmailCheckForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject', '')
            body = form.cleaned_data.get('body', '')
            raw_email = form.cleaned_data.get('raw_email', '')
            
            # Usar raw_email si se proporciona, sino usar subject + body
            if raw_email.strip():
                email_content = raw_email
            else:
                email_content = f"Subject: {subject}\n\n{body}"
            
            # Predecir
            result, error = spam_detector.predict(email_content)
            
            if result is None:
                messages.error(request, 
                    'El modelo no está entrenado. Por favor, entrena el modelo primero.')
                return redirect('index')
            
            # Guardar en la base de datos
            record = EmailCheckRecord.objects.create(
                email_content=email_content[:500],  # Guardar primeros 500 chars
                subject=subject[:255],
                prediction=result['label'],
                confidence=max(result['spam_probability'], result['ham_probability'])
            )
            
            # Pasar resultado al template
            return render(request, 'detector/result.html', {
                'result': result,
                'subject': subject,
                'form': EmailCheckForm(),
            })
    else:
        form = EmailCheckForm()
    
    return render(request, 'detector/index.html', {
        'form': form,
        'recent_checks': EmailCheckRecord.objects.all()[:10]
    })


def history(request):
    """Vista del historial de emails analizados."""
    records = EmailCheckRecord.objects.all()[:100]
    
    # Estadísticas
    total = records.count()
    spam_count = records.filter(prediction='spam').count()
    ham_count = records.filter(prediction='ham').count()
    
    stats = {
        'total': total,
        'spam': spam_count,
        'ham': ham_count,
        'spam_percentage': (spam_count / total * 100) if total > 0 else 0,
    }
    
    return render(request, 'detector/history.html', {
        'records': records,
        'stats': stats,
    })


def api_predict(request):
    """API REST para predicción."""
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            email_content = data.get('email_content', '')
            
            if not email_content:
                return JsonResponse({'error': 'Email content is required'}, status=400)
            
            result, error = spam_detector.predict(email_content)
            
            if result is None:
                return JsonResponse(
                    {'error': 'Model not trained'}, 
                    status=500
                )
            
            return JsonResponse(result)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'POST method required'}, status=405)


def model_info(request):
    """Información del modelo."""
    info = {
        'model_trained': spam_detector.classifier is not None,
        'vectorizer_features': len(spam_detector.get_feature_names()),
    }
    return render(request, 'detector/model_info.html', {'info': info})
