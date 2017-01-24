# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Servi\xc3\xa7o')),
                ('valor', models.CharField(max_length=20, verbose_name=b'Valor $')),
                ('CPU', models.IntegerField()),
                ('RAM', models.CharField(max_length=20, verbose_name=b'RAM')),
                ('SO', models.CharField(max_length=20, verbose_name=b'S.O.')),
                ('armazenamento', models.CharField(max_length=20, verbose_name=b'armazenamento')),
                ('scaleup', models.IntegerField(verbose_name=b'Scale Up')),
                ('scaledown', models.IntegerField(verbose_name=b'Scale Down')),
                ('datacenters', models.IntegerField(verbose_name=b'N\xc2\xba Datacenters')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
            ],
            options={
                'ordering': ['criado_em'],
                'verbose_name': 'nome',
                'verbose_name_plural': 'nomes',
            },
        ),
    ]
