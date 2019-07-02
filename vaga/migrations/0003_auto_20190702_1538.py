# Generated by Django 2.2.3 on 2019-07-02 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaga', '0002_auto_20190702_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vagamodel',
            options={'ordering': ['dt_update'], 'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
        migrations.RenameField(
            model_name='vagamodel',
            old_name='descricao',
            new_name='descrition',
        ),
        migrations.RenameField(
            model_name='vagamodel',
            old_name='dt_criacao',
            new_name='dt_create',
        ),
        migrations.RenameField(
            model_name='vagamodel',
            old_name='dt_modificacao',
            new_name='dt_update',
        ),
        migrations.RenameField(
            model_name='vagamodel',
            old_name='dt_validade',
            new_name='dt_validate',
        ),
        migrations.RenameField(
            model_name='vagamodel',
            old_name='titulo',
            new_name='title',
        ),
    ]
