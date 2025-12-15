from django.urls import path
from . import views

app_name = 'detector'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('model-info/', views.model_info, name='model_info'),
    path('api/predict/', views.api_predict, name='api_predict'),
]
