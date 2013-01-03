from django.conf.urls import patterns, include, url


#tastypie
from apps.standup.api import ProjectResource, ReportResource
project_resource = ProjectResource()
report_resource = ReportResource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^standup/', include('scrummager.apps.standup.urls')),

    #tastypie
    (r'^api/', include(project_resource.urls)),
    (r'^api/', include(report_resource.urls)),
)
