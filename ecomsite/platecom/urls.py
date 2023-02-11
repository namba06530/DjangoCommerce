from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'platecom'
urlpatterns = [
    path('', views.index, name='index'),
    path('produit/<str:slug>/', views.produit_detail, name='produit'),
    path('produits/', views.produits, name='produits'),
    path('search/', views.search, name='search'),
    path('login/', LoginView.as_view(next_page='/platecom/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/platecom/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('panier/', views.panier, name='panier'),
    path('add_to_cart/<int:produit_id>/', views.add_to_cart, name='add_to_cart'),
]
