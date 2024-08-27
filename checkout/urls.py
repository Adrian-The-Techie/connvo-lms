from django.urls import path

from .views import pay, transactionStatus

urlpatterns = [
    path("pay/", pay, name="pay"),
    path("transactionStatus", transactionStatus, name="transactionStatus"),
]
