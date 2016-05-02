from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView

#from .forms import CasaForm
from .models import Casa

class CasasList(ListView):
    model = Casa
