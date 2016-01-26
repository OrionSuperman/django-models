from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^interests/$', views.interests, name='interest'),
	url(r'^interests/(?P<id>\d+)/$', views.user, name='user'),
	url(r'^$', views.index, name='index')
)
