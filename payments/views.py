import uuid
from datetime import datetime

from decouple import config
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shared import generateRefNo

from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.


# Create your views here.


class PaymentView(APIView):
    @permission_classes([IsAuthenticated])
    # def post(self, request):
    #     print(request.data)
    #     program = Program(
    #         name=request.data["name"],
    #         description=request.data["description"],
    #         price=request.data["price"],
    #         url=uuid.uuid4(),
    #     )
    #     if request.FILES != None and request.FILES["thumbnail"] != None:
    #         program.thumbnail = request.data["thumbnail"]

    #     program.save()

    #     res = {"status": 1, "message": "Program added successfuly"}

    #     return JsonResponse(res)

    def get(self, request, url=None):

        if url == None:
            transactions = Transaction.objects.filter()
            serializedTransactions = TransactionSerializer(transactions, many=True)

            return JsonResponse({"status": 1, "data": serializedTransactions.data})

        else:
            try:
                transaction = Transaction.objects.get(url=url, visibility=True)
                serializedTransaction = TransactionSerializer(transaction)

                return JsonResponse({"status": 1, "data": serializedTransaction.data})

            except Transaction.DoesNotExist as e:
                return Response(
                    "Transaction not found", status=status.HTTP_404_NOT_FOUND
                )

    # @permission_classes([IsAuthenticated])
    # def put(self, request, url):
    #     try:
    #         program = Program.objects.get(url=url)

    #     except Program.DoesNotExist as e:
    #         return Response("Program not found", status=status.HTTP_404_NOT_FOUND)

    #     program.name = request.data["name"]
    #     program.description = request.data["description"]
    #     program.price = request.data["price"]
    #     program.date_updated = datetime.now()

    #     if request.FILES != None and request.FILES["thumbnail"] != None:
    #         program.thumbnail = request.data["thumbnail"]

    #     program.save()

    #     res = {"status": 1, "message": "Program edited successfuly"}

    #     return JsonResponse(res)

    # @permission_classes([IsAuthenticated])
    # def delete(self, request):

    #     for url in request.data["urls"]:
    #         try:
    #             program = Program.objects.get(url=url)

    #         except Program.DoesNotExist as e:
    #             return Response("Program not found", status=status.HTTP_404_NOT_FOUND)

    #         program.visibility = False

    #         program.save()

    #     res = {"status": 1, "message": "Program edited successfuly"}

    #     return JsonResponse(res)
