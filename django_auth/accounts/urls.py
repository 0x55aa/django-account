# coding: utf-8
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import (
    login,
    logout,
    password_change,
    password_change_done,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    )

from accounts import views
from accounts.forms import LoginForm, PasswordChangeForm


urlpatterns = patterns('',
    url(r'^login/$', login,
        {'authentication_form': LoginForm, 'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout,
        {'next_page': reverse_lazy('login')}, name='logout'),
    url(r'^password_change/$', password_change,
        {'template_name': 'accounts/password_change.html',
         'post_change_redirect': reverse_lazy('password_change_done'),
         'password_change_form': PasswordChangeForm},
        name='password_change'),
    url(r'^password_change_done/$', password_change_done,
        {'template_name': 'accounts/info.html', 'extra_context': {'info': '密码修改成功'}},
        name='password_change_done'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^profile/$', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),

    url(r'^password_reset/$', password_reset,
        {'template_name': 'accounts/password_reset_form.html',
            'email_template_name': 'accounts/password_reset_email.html',
            'subject_template_name': 'accounts/password_reset_subject.txt',
            'post_reset_redirect': reverse_lazy('password_reset_done')},
        name='password_reset'),
    url(r'^password_reset_done/$', password_reset_done,
        {'template_name': 'accounts/info.html', 'extra_context': {'info': '邮件已发送'}},
        name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'accounts/password_reset_confirm.html',
            'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'),
    url(r'^password_reset_complete/$', password_reset_complete,
        {'template_name': 'accounts/info.html',
         'extra_context': {'info': "修改成功"}},
        name='password_reset_complete'),
)
