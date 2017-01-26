from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_length', 'lnglat', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title']

    def content_length(self, post):
        return '{}글자'.format(len(post.content))
    content_length.short_description = '글자수'


admin.site.register(Post, PostAdmin)

