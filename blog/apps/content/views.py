from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from taggit.models import Tag
from blog.apps.content.models import Post


class PostList(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'content/post_detail.html'


class PostListTag(ListView):
    model = Post
    template_name = 'content/post_list_tag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug__iexact=self.kwargs['slug'])
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super(PostListTag, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context