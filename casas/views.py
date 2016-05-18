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
from pure_pagination.mixins import PaginationMixin

import time
import json
import datetime

from .forms import CasaForm
from .models import Casa, Favorito, Oferta
from usuarios.models import Perfil

class CasaUpdate(PaginationMixin, ListView):
    model = Casa
    login_url = '/login/'
    form_class = CasaForm
    redirect_field_name = 'redirect_to'
    context_object_name = 'casa'
    def get_queryset(self):
        base_qs = super(CasaUpdate, self).get_queryset()
        base_qs = Casa.objects.all().filter(owner=self.request.user, id=self.kwargs['pk'])
        print(base_qs)
        return base_qs

#Vista para mostrar la lista de todas las casas
class CasasList(PaginationMixin, ListView):
    model = Casa
    paginate_by = 5
    context_object_name = 'casas'
    #Filtra las todas las casas segun los parametros que recibe con el GET
    def get_queryset(self):
            result = super(CasasList, self).get_queryset()
            userId = self.request.GET.get('id')
            name = self.request.GET.get('name')
            city = self.request.GET.get('city')
            precioMin = self.request.GET.get('min-precio')
            precioMax = self.request.GET.get('max-precio')
            fechaIni = self.request.GET.get('fIni')
            fechaFin = self.request.GET.get('fFin')

            query = result
            if userId is not None:
                currentUser = User.objects.all().filter(id=userId).first()
                return result.filter(owner= userId)

            if precioMin is not None or precioMax is not None or fechaIni is not None or fechaFin is not None:
                query = Oferta.objects.all()
                if precioMin is not None:
                    query = query.exclude(precio__lt=precioMin)
                if precioMax is not None:
                    query = query.exclude(precio__gt=precioMax)
                if fechaIni is not None:
                    query = query.exclude(fechaInicio__lt=fechaIni)
                if fechaFin is not None:
                    query = query.exclude(fechaFin__gt=fechaFin)
                newquery = []
                for of in query:
                    houseID = of.casaOfertada_id
                    current = Casa.objects.all().filter(id=houseID).first()
                    if name is not None and name not in current.nombre:
                        continue
                    if city is not None and city not in current.ciudad:
                        continue
                    newquery.append(current)
                    query = newquery
            else:
                if name is not None:
                    query = query.filter(nombre__icontains=name)
                if city is not None:
                    query = query.filter(ciudad__icontains=city)
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
        finally:
            ultimas = Casa.objects.all().order_by('?')[:3]
            context = {
                'casas': ultimas,
                'favs1': len(Favorito.objects.all().filter(casaFavorito=ultimas[0])),
                'favs2': len(Favorito.objects.all().filter(casaFavorito=ultimas[1])),
                'favs3': len(Favorito.objects.all().filter(casaFavorito=ultimas[2])),
            }
    else:
        ultimas = Casa.objects.all().order_by('?')[:3]
        context = {
            'casas': ultimas,
            'favs1': len(Favorito.objects.all().filter(casaFavorito=ultimas[0])),
            'favs2': len(Favorito.objects.all().filter(casaFavorito=ultimas[1])),
            'favs3': len(Favorito.objects.all().filter(casaFavorito=ultimas[2])),
        }
    return render(request, 'index.jade', context)

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

def borrar_oferta(request):
    if request.method == 'POST':
        idOferta = request.POST.get('idOferta')

        if idOferta is not None:
            oferta = get_object_or_404(Oferta, pk=idOferta).delete()
            response_data = {

            }
            response_data['text'] = 'Oferta borrada correctamente'
            response_data['date'] = time.strftime("%H:%M:%S")
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

        else:
            return HttpResponse(
                json.dumps({'Error:': 'Los campos no son validos'}),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({'Error': 'No es del tipo POST'}),
            content_type="application/json"
        )
