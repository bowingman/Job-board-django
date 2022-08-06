from rest_framework import serializers

from .models import Job
from authapp.serializers import UserSerializer


class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "rate", "approved", "status", "user", "title", "description",
                  "company_scale", "company_tips", "job_info"]

    def create(self, validated_data):
        user = self.context['request'].user
        job = Job.objects.create(user=user, **validated_data)
        return job
