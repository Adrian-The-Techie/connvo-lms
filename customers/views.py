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

from .models import Customer
from .serializers import CustomerSerializer


from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


# Create your views here.


class SubscriberView(APIView):
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
            subscribers = Customer.objects.filter(visibility=True)
            serializedSubscribers = CustomerSerializer(subscribers, many=True)

            return JsonResponse({"status": 1, "data": serializedSubscribers.data})

        else:
            try:
                subscriber = Customer.objects.get(url=url, visibility=True)
                serializedSubscriber = CustomerSerializer(subscriber)

                return JsonResponse({"status": 1, "data": serializedSubscriber.data})

            except Customer.DoesNotExist as e:
                return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)

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



@api_view(['POST'])
def contactUs(request):
    data = request.data
    print(data)
    subject = data.get('subject')
    message = f"Name:{data.get('name')}\nEmail:{data.get('email')}\nSubject:{data.get('subject')}\nRequest type:{data.get('requestType')}\nMessage:{data.get('message')}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]
    
    send_mail( subject, message, email_from, recipient_list )
    
    return JsonResponse({'status':1, 'message':'Thank you for reaching out. We will reach out to you as soon as possible'})
