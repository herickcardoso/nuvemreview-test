# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20161205_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='SO',
            field=models.CharField(max_length=100, verbose_name=b'S.O.'),
        ),
    ]
