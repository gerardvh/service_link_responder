from django.conf.urls import patterns, include, url
from django.contrib import admin
import incident.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service_link_responder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), # currently unused
    url(r'^$', incident.views.index, name='index'), # currently unused
    url(r'^api/incident/', incident.views.incidentAPI, name='incidentAPI'),
    # Receives requests to the base url + 'api/incident/' 
    # runs incidentAPI() in views.py
    url(r'configuration$', incident.views.configuration, name='configuration')
    # Receives requests to the base url + 'configuration'
    # Returns a config json response for HipChat add-on installation
)
