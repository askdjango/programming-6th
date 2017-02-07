from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<pk>\d+)/$', views.post_detail),
]

