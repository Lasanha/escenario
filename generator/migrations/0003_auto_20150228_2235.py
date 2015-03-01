# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import generator.models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_auto_20150228_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escimg',
            name='img_id',
            field=models.CharField(default=generator.models.img_default, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='microblogpost',
            name='fixed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
