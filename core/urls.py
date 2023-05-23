from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chat.urls")),
    path("", include("authentication.urls"))
]


if settings.DEBUG:
    urlpatterns += [
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(r'static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT
        })
    ]