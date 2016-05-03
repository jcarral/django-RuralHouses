from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, PerfilForm
from .models import Casa

class CasasList(ListView):
    model = Casa

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Comprobar si existe el usuario en la bd
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print('Error al introducir los datos')
    else:
        return render(request, 'login.jade', {})

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def registrar_usuario(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        perfil_form = PerfilForm(data=request.POST)
        #Si los dos formularios son correctos
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            registrado = True
            return HttpResponseRedirect('/')
        else:
            print(user_form.errors, perfil_form.errors)
    #se crea el formulario para que el usuario pueda registrarse
    else:
        user_form = UserForm()
        perfil_form = PerfilForm()
        context = {
            'user_form' : user_form,
            'perfil_form': perfil_form,
            'registrado': registrado
        }
        return render(request, 'register.jade', context)
