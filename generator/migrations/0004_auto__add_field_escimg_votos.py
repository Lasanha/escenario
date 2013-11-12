# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EscImg.votos'
        db.add_column(u'generator_escimg', 'votos',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EscImg.votos'
        db.delete_column(u'generator_escimg', 'votos')


    models = {
        u'generator.esc': {
            'Meta': {'object_name': 'Esc'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'faltam': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'generator.escimg': {
            'Meta': {'object_name': 'EscImg'},
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'esc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['generator.Esc']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_id': ('django.db.models.fields.CharField', [], {'default': "'-6689643047485702348.jpg'", 'max_length': '50'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['generator']