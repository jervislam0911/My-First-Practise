__author__ = 'jervis'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^index$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^python/$', views.python, name='python'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^daily_life/$', views.thumbnail_list, name='thumbnail_list'),

]