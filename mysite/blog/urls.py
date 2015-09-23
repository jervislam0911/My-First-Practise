__author__ = 'jervis'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post_group/(?P<post_type>.*)/$', views.post_group, name='post_group'),
    # url(r'^(?P<pt>)/$', views.post_list, name='python_posts'),
    # url(r'^index$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^python/$', views.python, name='python'),
    url(r'^django/$', views.django, name='django'),
    url(r'^github/$', views.github, name='github'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^daily_life/$', views.thumbnail_list, name='thumbnail_list'),

]