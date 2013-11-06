from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from generator.urls import urlpatterns as gen_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'escenario.views.home', name='home'),
    # url(r'^escenario/', include('escenario.foo.urls')),

    url(r'', include(gen_urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_ROOT}),
    url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout_then_login', {}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    )

