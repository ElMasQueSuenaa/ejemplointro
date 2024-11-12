from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

# Vista para la página de inicio
def index(request):
    return redirect('login')

# Vista para mostrar el mensaje de usuario creado
def usuariocreado(request):
    return render(request, 'usuariocreado.html')

# Vista para registrar un nuevo usuario (usando 'register')
def registro(request):
    if request.method == 'POST':
        correo = request.POST.get('correo', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Validar que todos los campos están completos
        if not correo or not username or not password:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'register.html')

        # Validar que las contraseñas coinciden
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'register.html')

        # Verificar si el nombre de usuario ya existe
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, 'register.html')

        # Verificar si el correo ya está registrado
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            return render(request, 'register.html')

        # Crear el usuario
        Usuario.objects.create(correo=correo, username=username, contrasena=password)
        messages.success(request, "Usuario creado exitosamente.")
        return redirect('login')

    # Renderizar el formulario de registro
    return render(request, 'register.html')
