# Generated by Django 2.2.3 on 2019-07-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_auto_20190704_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculomodel',
            name='birth',
            field=models.DateTimeField(verbose_name='Nascimento'),
        ),
        migrations.AlterField(
            model_name='curriculomodel',
            name='genre',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], max_length=10, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(blank=True, choices=[('Candidato', 'Candidato'), ('Gestor', 'Gestor')], max_length=10, verbose_name='Type'),
        ),
    ]