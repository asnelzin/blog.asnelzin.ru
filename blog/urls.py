from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.apps.content.urls', namespace='content'))
)

if settings.DEBUG:
    urlpatterns += patterns('', ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('', url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico')))