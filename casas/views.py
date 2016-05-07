from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import UserForm, PerfilForm, CasaForm
from .models import Casa, Perfil


#Vista para mostrar la lista de todas las casas
class CasasList(ListView):
    model = Casa
    paginate_by = 3

#Actualizar el perfil del usuario
class UsuarioUpdate(UpdateView):
    model = Perfil
    fields = ['nombre', 'apellido', 'telefono', 'genero', 'nacimiento', 'avatar']

class CasaDetail(DetailView):
    model = Casa

#Iniciar sesion
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
            return HttpResponseRedirect('/login')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return render(request, 'login.jade', {})

#Cerrar sesion
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Vista para aniadir una casa nueva
@login_required(login_url='/login')
def nueva_casa(request):
    if request.method == 'POST':
        nueva_form = CasaForm(data=request.POST)
        if nueva_form.is_valid():
            casa = nueva_form.save(commit = False)
            casa.owner = request.user
            casa.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error")
    else:
        nueva_form = CasaForm()
    return render(request, 'casas/casa_nueva.jade', {'nueva_form': nueva_form,})




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
            return HttpResponseRedirect('/register')
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
