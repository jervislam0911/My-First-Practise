__author__ = 'jervis'
from django.conf.urls import url, patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

###############################################
# URL list for link design                    #
###############################################


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post_group/(?P<post_type>.*)/$', views.post_group, name='post_group'),
    url(r'^error/$', views.login_view, name='login_error'),
    url(r'^post/(?P<pk>[0-9]+)/post-section/$', views.post_section, name='post_section'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^python/$', views.python, name='python'),
    url(r'^django/$', views.django, name='django'),
    url(r'^github/$', views.github, name='github'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)