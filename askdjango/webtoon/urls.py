from django.conf.urls import url
from webtoon import views

urlpatterns = [
    url(r'^$', views.webtoon_list),
    url(r'^(?P<id>\d+)/$', views.webtoon_detail),
]

