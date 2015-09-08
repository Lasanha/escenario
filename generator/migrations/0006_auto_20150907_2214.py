# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_esc_criado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escimg',
            name='esc',
            field=models.OneToOneField(to='generator.Esc'),
        ),
    ]
