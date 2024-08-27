from django.db import models

from courses.models import Courses
from customers.models import Customer

# Create your models here.

TRANSACTION_STATUS = [
    (0, "INVALID"),
    (1, "COMPLETED"),
    (2, "FAILED"),
    (3, "REVERSED"),
    (4, "PENDING"),
]


class Transaction(models.Model):
    amount = models.FloatField()
    confirmation_code = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    reference_code = models.CharField(max_length=255, null=True)
    transaction_payload = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TRANSACTION_STATUS, null=True)
    date_updated = models.DateTimeField(null=True)
    order_tracking_id = models.CharField(max_length=255, null=True)
    payment_account = models.CharField(max_length=255, null=True)
    currency = models.CharField(max_length=255, null=True)
    payment_method = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ["-date_created"]
