from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.postgres import *

from .models import Produit
from .forms import ProduitSearchForm


def index(request):
    template = loader.get_template('platecom/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def produits(request):
    liste_des_produits = Produit.objects.all()
    context = {'liste_des_produits': liste_des_produits}
    return render(request, 'platecom/produits.html', context)


def search(request):
    form = ProduitSearchForm(request.GET)
    produits = []
    if form.is_valid():
        nom = form.cleaned_data['nom']
        produits = Produit.objects.filter(nom__icontains=nom)

    else:
        form = ProduitSearchForm()

    return render(request, 'platecom/search.html', {'form': form, 'produits': produits})
