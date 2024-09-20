from django.db import models


# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    is_online = models.BooleanField()
    ip = models.CharField(max_length=50)
    up_date_time = models.DateTimeField()

    def __str__(self):
        return self.name