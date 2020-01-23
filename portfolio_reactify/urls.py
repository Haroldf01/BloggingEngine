from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blogger.urls')),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
