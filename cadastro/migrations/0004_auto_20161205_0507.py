# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20161205_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='CPU',
            field=models.PositiveSmallIntegerField(verbose_name=b'CPU'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='RAM',
            field=models.PositiveSmallIntegerField(verbose_name=b'RAM'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='datacenters',
            field=models.PositiveSmallIntegerField(verbose_name=b'Datacenters'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='scaledown',
            field=models.PositiveSmallIntegerField(verbose_name=b'Scale Down'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='scaleup',
            field=models.PositiveSmallIntegerField(verbose_name=b'Scale Up'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='valor',
            field=models.PositiveSmallIntegerField(verbose_name=b'Valor'),
        ),
    ]
