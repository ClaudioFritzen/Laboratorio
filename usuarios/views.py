from django.shortcuts import render, HttpResponse, redirect

from django.contrib.messages import constants
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.WARNING, 'Senha deve ser maior que 6 digitos!')
            return redirect('/usuarios/cadastro')
        
        try:
            # Username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso!')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, tente mais tarde!!!')
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request,user)
            ## acontecerá um erro ao direcionamento
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
            return redirect('/usuarios/login')

