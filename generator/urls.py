from django.conf.urls import url, include
from generator.views import Home, About, List, Restricted, NewMicroblogPost
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^list/$', List.as_view(), name='list'),
    url(r'^sobre/$', About.as_view(), name='sobre'),
    url(r'^restricted/$', Restricted.as_view(), name='restricted'),
    url(r'^compose/$', NewMicroblogPost.as_view(), name='compose'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()

admin.autodiscover()
