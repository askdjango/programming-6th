from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
    }),
    url(r'^profile/$', views.profile, name='profile'),
]

