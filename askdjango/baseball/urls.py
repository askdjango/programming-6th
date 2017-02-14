from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blocks/(?P<pk>\d+)/$', views.block_detail, name='block_detail'),
]

