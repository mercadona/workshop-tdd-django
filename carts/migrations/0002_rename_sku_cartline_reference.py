# Generated by Django 4.2.1 on 2023-05-25 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartline',
            old_name='sku',
            new_name='reference',
        ),
    ]