from django.conf.urls import patterns, include, url
from views import Home, About, List, Restricted

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^view/(?P<esc_id>\d+)/$', Home.as_view()),
    url(r'^list/$', List.as_view()),
    url(r'^sobre/$', About.as_view()),
    url(r'^restricted/$', Restricted.as_view()),
)
