import uuid

from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from shared import generateRefNo

from .models import User

# Create your views here.


class UserView(APIView):
    def post(self, request):
        user = User(
            full_names=request.data["full_names"],
            email=request.data["email"],
            url=uuid.uuid4(),
            username=generateRefNo(),
            password=make_password(request.data["password"]),
        )

        user.save()

        res = {"status": 1, "message": "User created successfully"}

        return JsonResponse(res)


@api_view(["POST"])
def login(request):
    try:
        payload=request.data.get('cred')
        user = User.objects.get(email=payload["email"])
        if check_password(payload["password"], user.password) == False:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        else:
            token = Token.objects.get_or_create(user=user)[0].key

            response = {
                "status": 1,
                "message": "Login successful",
                "data": {
                    "user": {
                        "full_names": user.full_names,
                    },
                    "token": token,
                },
            }

        return JsonResponse(response)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )
