# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='CPU',
            field=models.DecimalField(verbose_name=b'CPU', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='RAM',
            field=models.DecimalField(verbose_name=b'RAM', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='armazenamento',
            field=models.DecimalField(verbose_name=b'Armazenamento', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='datacenters',
            field=models.DecimalField(verbose_name=b'Datacenters', max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='valor',
            field=models.DecimalField(verbose_name=b'Valor', max_digits=5, decimal_places=2),
        ),
    ]
