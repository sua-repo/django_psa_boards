from django.contrib import admin
from django.urls import include, path
from pybo import views

urlpatterns = [
    path("", views.index, name="index"),  # 기본 URL 패턴
]
