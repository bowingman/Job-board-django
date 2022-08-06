from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import JobSerializer
from .models import Job


class JobList(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    authentication_classes = [TokenAuthentication]


class JobDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = []
