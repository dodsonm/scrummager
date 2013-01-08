# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Standup'
        db.delete_table('standup_standup')

        # Adding model 'Report'
        db.create_table('standup_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yesterday', self.gf('django.db.models.fields.TextField')()),
            ('today', self.gf('django.db.models.fields.TextField')()),
            ('blockers', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('standup', ['Report'])


    def backwards(self, orm):
        # Adding model 'Standup'
        db.create_table('standup_standup', (
            ('blockers', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('today', self.gf('django.db.models.fields.TextField')()),
            ('yesterday', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('standup', ['Standup'])

        # Deleting model 'Report'
        db.delete_table('standup_report')


    models = {
        'standup.report': {
            'Meta': {'object_name': 'Report'},
            'blockers': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'today': ('django.db.models.fields.TextField', [], {}),
            'yesterday': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['standup']