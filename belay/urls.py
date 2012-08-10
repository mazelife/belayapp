from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from belay.site_views import Index


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name="index"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/passwords/',include('belay.utils.password_urls')
    ),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()