# Generated by Django 4.1 on 2023-02-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platecom', '0002_produit_stock_produit_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
