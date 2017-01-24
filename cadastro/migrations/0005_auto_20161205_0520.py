# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20161205_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='clockCPU',
            field=models.DecimalField(default=0, verbose_name=b'Clock', max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='RAM',
            field=models.DecimalField(verbose_name=b'RAM', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='valor',
            field=models.DecimalField(verbose_name=b'Valor $', max_digits=5, decimal_places=2),
        ),
    ]
