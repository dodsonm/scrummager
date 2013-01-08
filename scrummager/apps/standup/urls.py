from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template
from . import views


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {
            'template' : 'standup/workbench.html'
        })
)