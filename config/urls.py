from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/objectives', include('objectives.urls')),
    path('api/v1/users', include('users.urls')),
]
