from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    # default
    (r'^', include('%s.urls' % settings.APPNAME)),

)
