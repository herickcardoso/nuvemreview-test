# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20161205_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='SO',
            field=models.TextField(verbose_name=b'S.O.', choices=[(b'Linux', b'linux'), (b'Windows', b'windows'), (b'Ambos', b'ambos')]),
        ),
    ]
