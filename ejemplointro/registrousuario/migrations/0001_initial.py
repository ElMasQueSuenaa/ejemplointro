# Generated by Django 5.1.3 on 2024-11-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]