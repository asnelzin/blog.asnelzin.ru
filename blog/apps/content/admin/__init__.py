from django.contrib import admin
from blog.apps.content.models import Post
from blog.apps.content.admin.models import PostAdmin

admin.site.register(Post, PostAdmin)