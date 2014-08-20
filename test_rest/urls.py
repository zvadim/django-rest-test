from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^get_state/(?P<params>.+)', 'test_app.views.get_state', name='get_state'),
    url(r'^admin/', include(admin.site.urls)),
)
