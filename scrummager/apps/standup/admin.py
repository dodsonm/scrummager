from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Project, Report


class ReportInline(admin.StackedInline):
	model = Report

class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		ReportInline,
	]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Report)
