from django.conf.urls import include
from django.urls import path

from . import views


# from django.contrib import admin


urlpatterns = [
    path("health-check/", views.health_check, name="health_check"),
    path("", include("api.urls")),
    # path("admin/", admin.site.urls),
]
