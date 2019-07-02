# Generated by Django 2.2.3 on 2019-07-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GestorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('dt_create', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('dt_update', models.DateTimeField(auto_now=True, verbose_name='Atualizado em:')),
            ],
        ),
    ]
