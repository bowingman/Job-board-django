from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationList(ListCreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ApplicationDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
