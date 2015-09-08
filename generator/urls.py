from django.conf.urls import patterns, url
from generator.views import Home, About, List, Restricted, NewMicroblogPost
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^view/(?P<esc_id>\d+)/$', Home.as_view(), name='view'),
    url(r'^list/$', List.as_view(criterio='-criado_em'), name='list'),
    url(r'^rank/$', List.as_view(criterio='-votos'), name='rank'),
    url(r'^sobre/$', About.as_view(), name='sobre'),
    url(r'^restricted/$', Restricted.as_view(), name='restricted'),
    url(r'^compose/$', NewMicroblogPost.as_view(), name='compose'),

    # disabling api
    #url(r'^api/list/$', 'generator.views.api_list', name='api_list'),
    #url(r'^api/create/$', 'generator.views.api_create', name='api_create'),
    #url(r'^api/vote/(?P<escimg_id>\d+)$', 'generator.views.api_vote', name='api_vote'),
)

urlpatterns += staticfiles_urlpatterns()
