# Generated by Django 2.0.6 on 2019-09-04 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.CharField(max_length=35)),
                ('tipo_despesa', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=60)),
                ('forma_pagamento', models.CharField(max_length=40)),
                ('vencimento', models.DateField()),
                ('quitado', models.BooleanField()),
            ],
        ),
    ]
