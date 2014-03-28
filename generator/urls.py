from django.conf.urls import patterns, include, url
from views import Home, About, List, Restricted
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^view/(?P<esc_id>\d+)/$', Home.as_view()),
    url(r'^list/$', List.as_view(criterio='-criado_em')),
    url(r'^rank/$', List.as_view(criterio='-votos')),
    url(r'^sobre/$', About.as_view()),
    url(r'^restricted/$', Restricted.as_view()),
    url(r'^api/list/$', 'generator.views.api_list'),
    url(r'^api/create/$', 'generator.views.api_create'),
    url(r'^api/vote/(?P<escimg_id>\d+)$', 'generator.views.api_vote'),
)

urlpatterns += staticfiles_urlpatterns()
