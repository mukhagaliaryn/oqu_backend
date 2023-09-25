from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('summernote/', include('django_summernote.urls')),

    # apps...
    path('accounts/', include('accounts.urls')),
    path('', include('platforms.urls')),
    # path('products/', include('products.urls')),
    # path('profiles/', include('profiles.urls')),
]


urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]
