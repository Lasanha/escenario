# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('faltam', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EscImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('img_id', models.CharField(default=b'-364076195718487776.jpg', max_length=50)),
                ('votos', models.IntegerField(default=0)),
                ('esc', models.ForeignKey(to='generator.Esc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
