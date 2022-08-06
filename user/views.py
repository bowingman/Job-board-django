from re import U
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from authapp.models import User
from authapp.serializers import UserSerializer


class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
