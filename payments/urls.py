from django.urls import path

from .views import PaymentView

urlpatterns = [
    path("", PaymentView.as_view(), name="payments"),
    path("<str:url>", PaymentView.as_view(), name="payments"),
]
