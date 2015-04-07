from django.contrib import admin
from blog.apps.content.models import Post


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
