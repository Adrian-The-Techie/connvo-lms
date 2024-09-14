import uuid
import requests

from decouple import config
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customers.models import Customer
from payments.models import Transaction
from courses.models import Courses
from shared import generateRefNo

from .helpers.conversion import conversionToKES
from .helpers.pesapal import getTransactionStatus, submitOrder
from .helpers.p import disburse

# Create your views here.


@api_view(["POST"])
def pay(request):

    try:
        customerPayload = request.data["billing_address"]
        finalAmount = conversionToKES(request.data["program"]["price"])
        payload = {
            "id": generateRefNo(),
            "currency": "KES",
            "amount": finalAmount,
            "description": "Payment for {}".format(request.data["program"]["name"]),
            "redirect_mode": "PARENT_WINDOW",
            "callback_url": config("PESAPAL_CALLBACK_URL"),
            "cancellation_url": "",
            "notification_id": config("PESAPAL_NOTIFICATION_ID"),
            "billing_address": customerPayload,
        }

        res = submitOrder(payload)
        customer, created = Customer.objects.get_or_create(
            full_name=customerPayload["first_name"],
            phone=customerPayload["phone_number"],
            email=customerPayload["email_address"],
            address=customerPayload["line_1"],
            city=customerPayload["city"],
            state=customerPayload["state"],
            postal_code=customerPayload["postal_code"],
            zip_code=customerPayload["zip_code"],
            url=uuid.uuid4(),
        )
        transaction = Transaction(
            amount=payload["amount"],
            program=Courses.objects.get(id=request.data["program"]["id"]),
            order_tracking_id=res["order_tracking_id"],
            reference_code=payload["id"],
        )
        if created:
            transaction.customer = Customer.objects.filter(
                email=customerPayload["email_address"]
            ).first()

        else:
            transaction.customer = customer

        transaction.save()
        response = {
            "status": 1,
            "message": "Payment received successfuly",
            "data": res,
        }

        return JsonResponse(response)

    except Exception as e:
        return Response(
            {"status": 0, "error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
def transactionStatus(request):

    try:
        print(request)

        res = getTransactionStatus(request.GET["orderTrackingId"])
        transaction = Transaction.objects.get(
            order_tracking_id=request.GET["orderTrackingId"]
        )
        transaction.status = res["status_code"]
        transaction.confirmation_code = res["confirmation_code"]
        transaction.payment_account = res["payment_account"]
        transaction.currency = res["currency"]
        transaction.payment_method = res["payment_method"]

        transaction.save()
        response = {"status": 1, "message": "Transaction successful", "data": res}

        return JsonResponse(response)

    except Exception as e:
        return Response(
            {"status": 0, "error": e},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET'])
def q(request):

    res=disburse()

    return JsonResponse(res)

def c(request):

    print({"res":request.data})

    return JsonResponse({"res":request.data})