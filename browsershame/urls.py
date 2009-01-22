from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('browsershame.api.views',
    (r'^api/browser/get/(?P<name>[^/]+)', 'get_browser', {'major':None, 'minor':None, 'tick':None}),

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
