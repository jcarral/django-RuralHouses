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
    paginate_by = 5
    context_object_name = 'casas'
    #Filtra las todas las casas segun los parametros que recibe con el GET
    def get_queryset(self):
            result = super(CasasList, self).get_queryset()
            name = self.request.GET.get('name')
            city = self.request.GET.get('city')
            if name is not None and city is not None:
                query = result.filter(nombre__icontains=name, ciudad__icontains=city)
            elif name is not None:
                query = result.filter(nombre__icontains=name)
            elif city is not None:
                query = result.filter(ciudad__icontains=city)
            else:
                query = result
            return query

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
        except:
            perfil = Perfil(user=request.user)
            perfil.save()
    return render(request, 'index.jade', {})
