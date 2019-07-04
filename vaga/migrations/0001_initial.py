# Generated by Django 2.2.3 on 2019-07-04 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VagaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=100)),
                ('enterprise', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
                ('dt_validate', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dt_update'],
                'verbose_name_plural': 'Vagas',
                'verbose_name': 'Vaga',
            },
        ),
    ]
