# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Esc'
        db.create_table(u'generator_esc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.TextField')(max_length=25)),
            ('faltam', self.gf('django.db.models.fields.TextField')(max_length=20)),
            ('descricao', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'generator', ['Esc'])


    def backwards(self, orm):
        # Deleting model 'Esc'
        db.delete_table(u'generator_esc')


    models = {
        u'generator.esc': {
            'Meta': {'object_name': 'Esc'},
            'descricao': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'faltam': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.TextField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['generator']