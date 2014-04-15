from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('base.urls')),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'base/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),                 
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
