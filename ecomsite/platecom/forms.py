from django import forms
from .models import Produit


class ProduitSearchForm(forms.Form):
    nom = forms.CharField(label='Rechercher un produit', max_length=50)
