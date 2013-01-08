from tastypie.resources import ModelResource
from .models import Report, Project


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'

class ReportResource(ModelResource):
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'report'