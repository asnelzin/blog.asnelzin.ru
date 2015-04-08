from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.apps.content.models import Post


class PostList(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'content/post_detail.html'