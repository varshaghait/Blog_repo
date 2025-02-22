from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("username is taken")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])

        return validated_data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if not User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("account not found")

        return data

    def get_jwt_token(self, data):
        user = User.objects.get(username='varsh')
        if not user:
            return {"message": "invalid credentials", "data": {}}

        refresh = RefreshToken.for_user(user)

        return {
            "message": "Login success",
            "data": {
                "token": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            },
        }
