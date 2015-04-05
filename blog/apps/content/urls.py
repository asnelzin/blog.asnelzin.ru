from django.conf.urls import patterns, url
from blog.apps.content.views import PostList

urlpatterns = patterns(
    '',
    url(r'^$', PostList.as_view(), name='main')
)