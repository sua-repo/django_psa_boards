from django.contrib import admin
from django.urls import include, path


# http://127.0.0.1:8000
urlpatterns = [
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000
    path("pybo/", include("pybo.urls")),
]
