from datetime import datetime
from django.db import models

from authapp.models import User


class Job(models.Model):
    title = models.TextField()
    description = models.TextField()
    rate = models.IntegerField()
    approved = models.BooleanField(default=False)
    status = models.CharField(default="ready", max_length=30)
    company_scale = models.TextField()
    company_tips = models.TextField()
    job_info = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_jobs")
