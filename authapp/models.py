from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    name = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    role = models.CharField(max_length=20)
    title = models.TextField()
    description = models.TextField()
    rate = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    USERNAME_FIELD = "name"
