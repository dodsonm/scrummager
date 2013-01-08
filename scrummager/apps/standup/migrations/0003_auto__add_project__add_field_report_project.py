# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('standup_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('standup', ['Project'])

        # Adding field 'Report.project'
        db.add_column('standup_report', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['standup.Project']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('standup_project')

        # Deleting field 'Report.project'
        db.delete_column('standup_report', 'project_id')


    models = {
        'standup.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'standup.report': {
            'Meta': {'object_name': 'Report'},
            'blockers': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['standup.Project']"}),
            'today': ('django.db.models.fields.TextField', [], {}),
            'yesterday': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['standup']