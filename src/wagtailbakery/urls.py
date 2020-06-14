from django.urls import path

from .admin_views import index, publish

urlpatterns = [
    path('', index, name="index"),
    path('publish', publish, name="publish"),
]
