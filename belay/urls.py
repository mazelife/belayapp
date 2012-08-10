from django.conf import settings
from django.conf.urls import include, patterns, static, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'belay.views.home', name='home'),
    # url(r'^belay/', include('belay.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/passwords/',include('belay.utils.password_urls')
    ),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)