from rest_framework.serializers import ModelSerializer, RelatedField

from customers.serializers import CustomerSerializer
from courses.serializers import CoursesSerializer

from .models import Transaction


class TransactionSerializer(ModelSerializer):
    customer = CustomerSerializer()
    course = CoursesSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
