from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def perfil(request):
    return render(request, 'user/perfil.html')

def crear_usuario(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Se ha registrado exitosamente, ahora puedes iniciar Sesión con tu cuenta')
            form.save()
            return redirect ('index')

    return render(request, 'user/crear_usuario.html', {'form':form})

