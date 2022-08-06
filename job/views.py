from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

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
