from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, registro, usuariocreado

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', registro, name='register'),
    path('usuario_creado/', usuariocreado, name='usuario_creado'),
]
