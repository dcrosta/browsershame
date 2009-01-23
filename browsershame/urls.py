from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('browsershame.api.views',
    (r'^get/browser/(?P<name>[^/]+)/(?P<major>[^/]+)/(?P<minor>[^/]+)/(?P<tick>[^/]+)', 'get_browser'),
    (r'^get/browser/(?P<name>[^/]+)/(?P<major>[^/]+)/(?P<minor>[^/]+)', 'get_browser', {'tick':None}),
    (r'^get/browser/(?P<name>[^/]+)/(?P<major>[^/]+)', 'get_browser', {'minor':None, 'tick':None}),

    (r'^list/browser/(?P<name>[^/]+)/(?P<major>[^/]+)/(?P<minor>[^/]+)/(?P<tick>[^/]+)', 'list_browsers'),
    (r'^list/browser/(?P<name>[^/]+)/(?P<major>[^/]+)/(?P<minor>[^/]+)', 'list_browsers', {'tick':None}),
    (r'^list/browser/(?P<name>[^/]+)/(?P<major>[^/]+)', 'list_browsers', {'minor':None, 'tick':None}),
    (r'^list/browser/(?P<name>[^/]+)', 'list_browsers', {'name':None, 'minor':None, 'tick':None}),

)

urlpatterns += patterns('',
    # Example:
    # (r'^browsershame/', include('browsershame.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
