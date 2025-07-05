from django.urls import path
from . import views

app_name = 'core'  # Namespace para evitar conflictos

urlpatterns = [
    path('', views.index, name='index'),  # URL principal (ej: 127.0.0.1:8000/)
    path('del/<str:item_id>/', views.remove, name='remove'),  # URL para eliminar
]