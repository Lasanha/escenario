# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_esc_origem'),
    ]

    operations = [
        migrations.AddField(
            model_name='esc',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 9, 8, 2, 52, 48, 313326, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
