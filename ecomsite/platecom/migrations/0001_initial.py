# Generated by Django 4.1 on 2023-01-27 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('produit_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('categorie', models.CharField(blank=True, max_length=50, null=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fournisseur', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'produit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'role',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('utilisateur_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('mail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='platecom.role')),
            ],
            options={
                'db_table': 'utilisateur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('panier_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='platecom.produit')),
            ],
            options={
                'db_table': 'panier',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('commande_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('panier', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='platecom.panier')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='platecom.utilisateur')),
            ],
            options={
                'db_table': 'commande',
                'managed': True,
            },
        ),
    ]
