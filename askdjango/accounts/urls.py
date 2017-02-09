from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]

