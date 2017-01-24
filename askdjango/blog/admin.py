from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'lnglat', 'map']

    def map(self, post):
        if post.lnglat:
            lng, lat = post.lnglat.split(',')
            url = 'https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=13&size=75x75&maptype=roadmap&markers=color:blue%7Clabel:S%7C{lat},{lng}'.format(lat=lat, lng=lng)
            return '<img src="{}" />'.format(url)
    map.allow_tags = True

admin.site.register(Comment)
