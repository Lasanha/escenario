from django.conf.urls import patterns, include, url
from views import Home

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^view/(?P<esc_id>\d+)/$', Home.as_view()),
)
