# dev_13
from django.urls import path
from django.contrib.auth import views as auth_views

from common import views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),  # dev_13
    path("logout/", views.logout_view, name="logout"),  # dev_13
    path("signup/", views.signup, name="signup"),  # dev_15
]
