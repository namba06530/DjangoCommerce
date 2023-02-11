from django.db import models
from django.urls import reverse

class Commande(models.Model):
    commande_id = models.SmallAutoField(primary_key=True)
    panier = models.OneToOneField('Panier', models.DO_NOTHING)
    utilisateur = models.ForeignKey('Utilisateur', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'commande'


class Panier(models.Model):
    panier_id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    produit = models.ForeignKey('Produit', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'panier'


class Produit(models.Model):
    produit_id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, null=True)
    categorie = models.CharField(max_length=50, blank=True, null=True)
    prix = models.FloatField(default=0.0)
    fournisseur = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    """
    - la quantité en stock
    - Image
    - prix = models.DecimalField(max_digits=7, decimal_places=2)
    - description = models.CharField(max_length=500, blank=True, null=True)
    """

    def __str__(self):
        template = '{0.nom}'
        return template.format(self)


    def get_absolute_url(self):
        return reverse("platecom:produit", kwargs={"slug": self.slug})


    class Meta:
        managed = True
        db_table = 'produit'


class Role(models.Model):
    role_id = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'role'


class Utilisateur(models.Model):
    utilisateur_id = models.SmallAutoField(primary_key=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    def __str__(self):
        template = '{0.prenom} {0.nom}'
        return template.format(self)

    class Meta:
        managed = True
        db_table = 'utilisateur'
