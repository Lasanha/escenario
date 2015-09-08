# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_auto_20150228_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='esc',
            name='origem',
            field=models.GenericIPAddressField(default=''),
        ),
    ]
