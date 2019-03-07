# Generated by Django 2.1.7 on 2019-03-07 11:23

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
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personalizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tempo', models.IntegerField(default=0, help_text='Tempo em minutos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personalizacao', models.ManyToManyField(blank=True, to='pizzaria.Personalizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tempo', models.IntegerField(default=0, help_text='Tempo em minutos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tempo', models.IntegerField(default=0, help_text='Tempo em minutos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pizza',
            name='sabor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaria.Sabor'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaria.Tamanho'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pizza',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzaria.Pizza'),
        ),
    ]
