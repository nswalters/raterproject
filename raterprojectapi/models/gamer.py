from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Gamer(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
