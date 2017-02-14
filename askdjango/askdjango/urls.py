"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from blog import views as blog_views
from webtoon import views as webtoon_views

# def root(request):
#     return redirect('post_list')

urlpatterns = [
    # url(r'^$', root),
    url(r'^$', lambda request: redirect('blog:post_list')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),  # namespace 를 걸지않습니다.
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^webtoon/', include('webtoon.urls', namespace='webtoon')),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

