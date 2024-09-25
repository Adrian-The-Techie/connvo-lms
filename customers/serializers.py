from rest_framework.serializers import ModelSerializer

from courses.serializers import LessonSerializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    courses = LessonSerializer(many=True)
    class Meta:
        model = Customer
        fields = "__all__"
