
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("signup/",register, name="signup"),
    path("login/",login_view, name="login"),
    path("logout/",logout_user, name="logout")
]
