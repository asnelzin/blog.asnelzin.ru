from __future__ import unicode_literals

from django.views.generic import ListView
from blog.apps.content.models import Post


class PostList(ListView):
    model = Post
    template_name = 'index.html'