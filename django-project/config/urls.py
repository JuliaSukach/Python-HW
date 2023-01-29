# import main.views as main

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # main urls
    path('', include('main.urls')),

    # admin urls
    path('admin/', admin.site.urls),

    # API urls
    path('', include('api.urls')),
    path('api/authentication/', include('authentication.urls')),

    # AUTH endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


