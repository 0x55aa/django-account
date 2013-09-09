# coding: utf-8
from django.conf.urls import patterns, url

from board.views import BoardListView, AddMessageView


urlpatterns = patterns('',
    url(r'^add_message/$', AddMessageView.as_view(), name='add_message'),
    url(r'^list/$', BoardListView.as_view(), name='message_list'),

)
