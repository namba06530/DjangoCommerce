from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitSearchForm
from django.contrib.auth import get_user_model, login

User = get_user_model()


def index(request):
    liste_produits = Produit.objects.all()
    context = {"liste_produits": liste_produits}
    return render(request, 'platecom/index.html', context)


def produit_detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    context = {'produit': produit}
    return render(request, 'platecom/detail.html', context)


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


def add_to_cart(request, produit_id):
    produit = get_object_or_404(Produit, produit_id=produit_id)
    panier = request.session.get('panier', [])
    total = produit.prix
    for article in panier:
        if article['produit_id'] == produit_id:
            article['quantite'] += 1
            article['total'] = article['quantite'] * produit.prix
            request.session['panier'] = panier
            return redirect(request.META.get('HTTP_REFERER'))
    panier.append({
        'produit_id': produit_id,
        'nom': produit.nom,
        'quantite': 1,
        'prix': str(produit.prix),
        'total': total
    })
    request.session['panier'] = panier
    # Rediriger vers la page précédente
    return redirect(request.META.get('HTTP_REFERER'))


def panier(request):
    # Récupérer le panier stocké dans la session
    panier = request.session.get('panier', [])
    # Récupérer les produits de la base de données
    produits = Produit.objects.filter(produit_id__in=[article['produit_id'] for article in panier])
    if not panier:
        message = "Le panier est vide."
        return render(request, 'platecom/panier.html', {'message': message})
    else:
        return render(request, 'platecom/panier.html', {'panier': panier, 'produits': produits})


def delete_panier(request):
    panier = request.session.get('panier', [])
    if panier:
        request.session.pop('panier', None)
    return redirect('platecom:panier')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('platecom:index')
    else:
        return render(request, 'registration/signup.html')
