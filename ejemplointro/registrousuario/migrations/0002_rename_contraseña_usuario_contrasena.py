# Generated by Django 5.1.3 on 2024-11-12 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrousuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
