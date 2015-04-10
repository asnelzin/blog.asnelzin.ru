from django.contrib import admin
from blog.apps.media.models import Media
from blog.apps.media.admin.models import MediaAdmin

admin.site.register(Media, MediaAdmin)