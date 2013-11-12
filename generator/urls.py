from django.conf.urls import patterns, include, url
from views import Home, About, List, Restricted
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^view/(?P<esc_id>\d+)/$', Home.as_view()),
    url(r'^list/$', List.as_view()),
    url(r'^sobre/$', About.as_view()),
    url(r'^restricted/$', Restricted.as_view()),
    url(r'^api/list/$', 'generator.views.api_list'),
    url(r'^api/create/$', 'generator.views.api_create'),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
