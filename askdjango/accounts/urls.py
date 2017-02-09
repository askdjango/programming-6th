from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
    }),
    url(r'^logout/$', logout, name='logout', kwargs={
        'next_page': settings.LOGIN_URL,
    }),
    url(r'^profile/$', views.profile, name='profile'),
]

