from django.urls import path

from .views import UserView, login

urlpatterns = [
    path("", UserView.as_view(), name="programs"),
    path("login/", login, name="login"),
]
