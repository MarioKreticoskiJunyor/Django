from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    usuarios = {
        'usuarios': usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
