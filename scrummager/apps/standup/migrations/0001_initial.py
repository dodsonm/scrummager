# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Standup'
        db.create_table('standup_standup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yesterday', self.gf('django.db.models.fields.TextField')()),
            ('today', self.gf('django.db.models.fields.TextField')()),
            ('blockers', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('standup', ['Standup'])


    def backwards(self, orm):
        # Deleting model 'Standup'
        db.delete_table('standup_standup')


    models = {
        'standup.standup': {
            'Meta': {'object_name': 'Standup'},
            'blockers': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'today': ('django.db.models.fields.TextField', [], {}),
            'yesterday': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['standup']