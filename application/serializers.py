from dataclasses import field
from rest_framework import serializers

from .models import Application
from job.models import Job
from job.serializers import JobSerializer
from authapp.serializers import UserSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ["id", "rate", "content", "job", "user", "answer", "answered"]

    def create(self, validated_data):
        user = self.context['request'].user
        job = Job.objects.filter(
            id=self.context['request'].data['job_id']).first()
        application = Application.objects.create(
            user=user, job=job, **validated_data)
        return application
