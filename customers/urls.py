from django.urls import path

from .views import SubscriberView

urlpatterns = [
    path("", SubscriberView.as_view(), name="subscribers"),
    path("<str:url>", SubscriberView.as_view(), name="subscriber"),
]
