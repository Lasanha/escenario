# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EscImg'
        db.create_table(u'generator_escimg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('esc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['generator.Esc'])),
            ('img_id', self.gf('django.db.models.fields.CharField')(default='2013-11-04 13:26:59.468753jpg', max_length=50)),
        ))
        db.send_create_signal(u'generator', ['EscImg'])

        # Deleting field 'Esc.criado_em'
        db.delete_column(u'generator_esc', 'criado_em')


    def backwards(self, orm):
        # Deleting model 'EscImg'
        db.delete_table(u'generator_escimg')


        # User chose to not deal with backwards NULL issues for 'Esc.criado_em'
        raise RuntimeError("Cannot reverse this migration. 'Esc.criado_em' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Esc.criado_em'
        db.add_column(u'generator_esc', 'criado_em',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True),
                      keep_default=False)


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
            'img_id': ('django.db.models.fields.CharField', [], {'default': "'2013-11-04 13:27:03.674865jpg'", 'max_length': '50'})
        }
    }

    complete_apps = ['generator']