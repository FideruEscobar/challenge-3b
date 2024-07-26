from django.contrib import admin
from django.urls import path, include
from tiendastres import urls as tiendastres_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(tiendastres_urls)),
]
