import hashlib
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserSerializer


class SignIn(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        password = request.data.get('password')
        if not name or not password:
            return Response(
                {
                    'name, password': [
                        'This fields are required.'
                    ]
                },
                status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(name=name).first()

        if (user.password != hashlib.sha224(password.encode('ascii')).hexdigest()):
            return Response({
                'detail': ['Wrong Password!'], },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user:
            return Response(
                {
                    'detail': [
                        'Invalid Credentials'
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = Token.objects.filter(user_id=user.id).first()
            if token:
                Token.objects.filter(user_id=user.id).delete()
        finally:
            token = Token.objects.create(user=user)
            return Response(
                {
                    'token': token.key,
                    'user': {
                        'id': user.id,
                        'name': user.name,
                        'title': user.title,
                    }
                },
                status=status.HTTP_200_OK
            )


class SignUp(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        role = request.data.get('role')
        title = request.data.get('title')
        description = request.data.get('description')
        if not name or not password or not role or not title or not description:
            return Response(
                {
                    'name, password': [
                        'This fields are required.'
                    ]
                },
                status.HTTP_400_BAD_REQUEST
            )

        hashed_password = hashlib.sha224(password.encode('ascii')).hexdigest()

        userSerializer = UserSerializer(data={
            'name': name,
            'password': hashed_password,
            'role': role,
            'title': title,
            'description': description,
            'rate': 0,
            'approved': False,
            'last_login': datetime.now(),
        })
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        return Response(
            {
                'user': userSerializer.data
            },
            status=status.HTTP_200_OK
        )
