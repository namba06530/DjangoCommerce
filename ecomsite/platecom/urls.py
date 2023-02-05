from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'platecom'
urlpatterns = [
    path('', views.index, name='index'),
    path('produits/', views.produits, name='produits'),
    path('search/', views.search, name='search'),
    path('login/', LoginView.as_view(next_page='/platecom/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/platecom/'), name='logout'),
]
