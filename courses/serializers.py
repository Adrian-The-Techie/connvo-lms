from rest_framework.serializers import ModelSerializer

from .models import Courses, Chapter, Lesson


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


