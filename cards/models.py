from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=255)
    is_online = models.BooleanField()
    ip = models.GenericIPAddressField()
    up_date_time = models.DateTimeField()
    port = models.PositiveIntegerField(default=80)
    login = models.CharField(max_length=255)
    password = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name