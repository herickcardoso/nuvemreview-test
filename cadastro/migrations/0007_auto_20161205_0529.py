# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20161205_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='RAM',
            field=models.DecimalField(verbose_name=b'RAM', max_digits=5, decimal_places=1),
        ),
    ]
