# sso/urls.py

from django.urls import path
from . import views

app_name = "sso"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("unauthorized", views.unauthorized, name="unauthorized"),
]
