from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from django.views.static import serve as static_serve
from django_summernote import urls as summernote_urls

from generator.urls import urlpatterns as gen_urls

admin.autodiscover()

urlpatterns = [
    url(r'', include(gen_urls)),
    url(r'^summernote/', include(summernote_urls)),
    url(r'^static/(?P<path>.*)$', static_serve, {'document_root': settings.STATIC_ROOT}),
    url(r'login/$', login, {'template_name': 'login.html'}),
    url(r'logout/$', logout_then_login, {}),
]
