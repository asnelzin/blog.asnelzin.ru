from django.conf.urls import patterns, url
from blog.apps.content.views import PostList, PostDetail, PostListTag

urlpatterns = patterns(
    '',
    url(r'^$', PostList.as_view(), name='main'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetail.as_view(), name='post_view'),
    url(r'^tags/(?P<slug>[-_\w]+)/$', PostListTag.as_view(), name='post_list_tag')
)