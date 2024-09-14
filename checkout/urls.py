from django.urls import path

from .views import pay, transactionStatus, q, c

urlpatterns = [
    path("pay/", pay, name="pay"),
    path("transactionStatus", transactionStatus, name="transactionStatus"),
    path("q/", q, name="q"),
    path("c/", c, name="c"),
]
