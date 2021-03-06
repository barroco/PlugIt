# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import django.contrib.auth


urlpatterns = patterns('',

	url(r'^ebuio_logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^ebuio_login$', 'django.contrib.auth.views.login'),

)

urlpatterns += patterns(
	'plugIt.views',
    url(r'^media/(?P<path>.*)$', 'media'),
    url(r'^ebuio_setUser$', 'setUser'),
    url(r'^ebuio_setOrga$', 'setOrga'),


    
    url(r'^ebuio_api/$', 'api_home'),
    url(r'^ebuio_api/user/(?P<userPk>[\-0-9]*)$', 'api_user'),
    url(r'^ebuio_api/orga/(?P<orgaPk>[\-0-9]*)$', 'api_orga'),

    url(r'^(?P<query>.*)$', 'main'),
)
