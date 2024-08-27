from django.urls import path

from .views import CourseView, LessonView

urlpatterns = [
    path("lessons/", LessonView.as_view(), name="lesson"),
]
