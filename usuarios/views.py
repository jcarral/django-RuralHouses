from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import UserForm, PerfilForm
from .models import Perfil
from casas.models import Casa, Favorito


#Actualizar el perfil del usuario
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Perfil
    login_url = '/login/'
    form_class = PerfilForm
    redirect_field_name = 'redirect_to'
    def form_valid(self, form):
        self.object.save()
        messages.success(self.request, 'Datos actualizados correctamente')
        return HttpResponseRedirect(self.get_success_url())
    def get_queryset(self):
        base_qs = super(UsuarioUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class UsuarioFicha(DetailView):
    model = Perfil
    context_object_name = 'perfil'
    def get_context_data(self, **kwargs):
        context = super(UsuarioFicha, self).get_context_data(**kwargs)
        context['casas'] = Casa.objects.all().filter(owner__perfil=context['perfil'])
        context['favoritos'] = Favorito.objects.all().filter(usuarioFavorito__perfil=context['perfil'])
        return context

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
            messages.error(request, 'El usuario que intentas introducir no existe o la contrasenia no es correcta')
            return HttpResponseRedirect('/login')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return render(request, 'usuarios/login.jade', {})
#Cerrar sesion
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
            messages.error(request, 'Hay campos incorrectos')
            return HttpResponseRedirect('/signup')
    #se crea el formulario para que el usuario pueda registrarse
    else:
        user_form = UserForm()
        perfil_form = PerfilForm()
        context = {
            'user_form' : user_form,
            'perfil_form': perfil_form,
            'registrado': registrado
        }
        return render(request, 'usuarios/register.jade', context)
