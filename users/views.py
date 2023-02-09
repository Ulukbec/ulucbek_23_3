from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserValidateSerializer, UserCreateSerializer
from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request):
        serializers = UserCreateSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        User.objects.create_user(**serializers.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class AuthorizationsAPIView(APIView):
    def post(self, request):
        serializers = UserValidateSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = authenticate(**serializers.validated_data)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)
