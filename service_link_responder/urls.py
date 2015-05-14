from django.conf.urls import patterns, include, url
from django.contrib import admin
import incident.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service_link_responder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', incident.views.index, name='index'),
    url(r'^api/incident', incident.views.incident, name='incident'),
    url(r'configuration$', incident.views.configuration, name='configuration')
)
