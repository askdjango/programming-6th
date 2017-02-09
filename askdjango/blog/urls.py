from django.conf.urls import url
from blog import views
from blog import views_cbv

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),   # TODO: + comment_list
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    # TODO: comment_new
    # TODO: comment_edit
    # TODO: comment_delete
]

