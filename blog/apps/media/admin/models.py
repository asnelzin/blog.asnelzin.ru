from django.contrib import admin
from blog.apps.media.models import Media


class MediaAdmin(admin.ModelAdmin):
    class Meta:
        model = Media
