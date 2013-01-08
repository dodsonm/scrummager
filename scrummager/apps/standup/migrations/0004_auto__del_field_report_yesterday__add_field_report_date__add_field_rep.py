# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Report.yesterday'
        db.delete_column('standup_report', 'yesterday')

        # Adding field 'Report.date'
        db.add_column('standup_report', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 1, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Report.previous_day'
        db.add_column('standup_report', 'previous_day',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Report.created'
        db.add_column('standup_report', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 1, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Report.updated'
        db.add_column('standup_report', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 3, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Report.yesterday'
        db.add_column('standup_report', 'yesterday',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Report.date'
        db.delete_column('standup_report', 'date')

        # Deleting field 'Report.previous_day'
        db.delete_column('standup_report', 'previous_day')

        # Deleting field 'Report.created'
        db.delete_column('standup_report', 'created')

        # Deleting field 'Report.updated'
        db.delete_column('standup_report', 'updated')


    models = {
        'standup.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'standup.report': {
            'Meta': {'object_name': 'Report'},
            'blockers': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previous_day': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['standup.Project']"}),
            'today': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['standup']