from django.conf.urls import patterns, url, include

from geonode.urls import urlpatterns

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'wfp.views.index', {'template': 'site_index.html'}, name='home'),
 
 ) + \
urlpatterns