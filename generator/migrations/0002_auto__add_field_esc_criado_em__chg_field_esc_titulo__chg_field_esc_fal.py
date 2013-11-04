# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Esc.criado_em'
        db.add_column(u'generator_esc', 'criado_em',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 4, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'Esc.titulo'
        db.alter_column(u'generator_esc', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Esc.faltam'
        db.alter_column(u'generator_esc', 'faltam', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Esc.descricao'
        db.alter_column(u'generator_esc', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Esc.criado_em'
        db.delete_column(u'generator_esc', 'criado_em')


        # Changing field 'Esc.titulo'
        db.alter_column(u'generator_esc', 'titulo', self.gf('django.db.models.fields.TextField')(max_length=25))

        # Changing field 'Esc.faltam'
        db.alter_column(u'generator_esc', 'faltam', self.gf('django.db.models.fields.TextField')(max_length=20))

        # Changing field 'Esc.descricao'
        db.alter_column(u'generator_esc', 'descricao', self.gf('django.db.models.fields.TextField')(max_length=200))

    models = {
        u'generator.esc': {
            'Meta': {'object_name': 'Esc'},
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'faltam': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['generator']