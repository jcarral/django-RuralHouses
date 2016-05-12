from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import time
import json
import datetime

from .forms import CasaForm
from .models import Casa, Favorito, Oferta
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
    context_object_name = 'casa'
    def get_context_data(self, **kwargs):
        context = super(CasaDetail, self).get_context_data(**kwargs)
        context['ofertas'] = Oferta.objects.all().filter(casaOfertada=context['casa'])
        if self.request.user.is_authenticated():
            context["fav"] = len(Favorito.objects.all().filter(usuarioFavorito=self.request.user, casaFavorito=context['casa']))
        return context

#Vista para aniadir una casa nueva

class NuevaCasa(LoginRequiredMixin, CreateView):
    model = Casa
    login_url = '/login/'
    form_class = CasaForm
    redirect_field_name = 'redirect_to'
    def form_valid(self, form):
        form.instance.owner =self.request.user
        form.save()
        messages.success(self.request, 'Casa creada correctamente')
        return super(NuevaCasa, self).form_valid(form)


def index(request):

    if request.method == 'GET' and request.user and request.user.is_authenticated():
        try:
            user = request.user
            perfil = request.user.perfil
        except:
            perfil = Perfil(user=request.user)
            perfil.save()
    return render(request, 'index.jade', {})

def gestionar_favoritos(request):
    if request.method == 'POST':
        author = request.user
        casaID = request.POST.get('id')
        casa = Casa.objects.all().filter(id=casaID).first()
        favs = Favorito.objects.all().filter(casaFavorito=casa, usuarioFavorito=author)
        if len(favs) == 0:
            fav = Favorito(casaFavorito=casa, usuarioFavorito=author)
            fav.save()
            response_data = {
            }
            response_data['text'] = 'Fav creado correctamente'
            response_data['date'] = time.strftime("%H:%M:%S")
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            favs.delete()
            return HttpResponse(
                json.dumps({"text": "Borrada"}),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def crear_oferta(request):

    if request.method == 'POST':
        print(request.POST)
        author = request.user
        casaID = request.POST.get('id')
        fechaInicio = request.POST.get('first')
        fechaFin = request.POST.get('last')
        precio = request.POST.get('precio')
        casa = Casa.objects.all().filter(id=casaID, owner=author).first()
        if casa is not None and fechaFin is not None and fechaInicio is not None:
            oferta = Oferta(fechaInicio=fechaInicio, fechaFin=fechaFin, precio=precio, casaOfertada=casa)
            oferta.save()
            response_data = {
            }
            response_data['text'] = 'Oferta creada correctamente'
            response_data['date'] = time.strftime("%H:%M:%S")
            print("Funciona")
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:

            return HttpResponse(
                json.dumps({'Error:': 'Los campos no son validos'}),
                content_type="application/json"
            )
    print("Error 2")
    return HttpResponse(
        json.dumps({'Error': 'No es del tipo POST'}),
        content_type="application/json"
    )
