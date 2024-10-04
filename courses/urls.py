from django.urls import path

from .views import CourseView, LessonView, ChapterView

urlpatterns = [
    path("", CourseView.as_view(), name="course"),
    path("chapters/", ChapterView.as_view(), name="chapter"),
    path("lessons/", LessonView.as_view(), name="lesson"),
]
