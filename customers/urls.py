from django.urls import path

from .views import SubscriberView, contactUs

urlpatterns = [
    path("", SubscriberView.as_view(), name="subscribers"),
    path("<str:url>", SubscriberView.as_view(), name="subscriber"),
    path("contactUs/", contactUs, name="contactUs"),
]
