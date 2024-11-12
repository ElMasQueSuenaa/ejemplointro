from django.contrib import admin
from django.urls import path, include
from registrousuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registrousuario.urls')),
]
