from django.contrib import admin
from django.urls import include, path
from pybo import views

# "http://127.0.0.1:8000
urlpatterns = [
    path("admin/", admin.site.urls),  # "http://127.0.0.1:8000/admin/
    # path("pybo/", views.index),  # dev_1
    path("pybo/", include("pybo.urls")),  # dev_1
    path("hello/", views.hello),  # dev_1
]
