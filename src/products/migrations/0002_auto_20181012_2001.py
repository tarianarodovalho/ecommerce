# Generated by Django 2.1.2 on 2018-10-12 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='preco',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='titulo',
        ),
    ]
