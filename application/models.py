from operator import mod
from turtle import ondrag
from django.db import models

from authapp.models import User
from job.models import Job


class Application(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="application_applications"
    )
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="application_applications"
    )
    content = models.TextField()
    rate = models.IntegerField()
    answer = models.TextField(null=True)
    answered = models.BooleanField(default=False)
