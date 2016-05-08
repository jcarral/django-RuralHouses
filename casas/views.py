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


from .forms import CasaForm
from .models import Casa
from usuarios.models import Perfil

#Vista para mostrar la lista de todas las casas
class CasasList(ListView):
    model = Casa
    paginate_by = 3

class CasaDetail(DetailView):
    model = Casa


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

def index(request):

    if request.method == 'GET' and request.user and request.user.is_authenticated():
        try:

            user = request.user
            perfil = request.user.perfil
            print ("Tiene perfil")
        except:
            perfil = Perfil(user=request.user)
            perfil.save()
            print ("NO Tiene perfil")
    return render(request, 'index.jade', {})
