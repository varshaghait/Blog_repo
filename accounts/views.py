from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers import LoginSerializer, RegisterSerializer


# Create your views here.
class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {"data": serializer.errors, "message": "something went wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()

            return Response(
                {"data": {}, "message": "your account is created"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"data": {}, "message": "error got"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            print(data)
            if not serializer.is_valid():
                return Response(
                    {"data": serializer.errors, "message": "something went wrong"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            response = serializer.get_jwt_token(serializer.data)
            print("RESPONSE : ",response)
            return Response(response, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response(
                {"data": {}, "message": "something went wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )
