# Generated by Django 5.0.2 on 2024-09-09 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('idCliente', models.PositiveIntegerField()),
                ('creationDate', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('emailCliente', models.EmailField(max_length=60, verbose_name='email')),
                ('telefonoCliente', models.CharField(max_length=100, null=True, verbose_name='Telefono del Cliente')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clientes',
                'ordering': ['creationDate'],
            },
        ),
    ]
