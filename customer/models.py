from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class customer(models.Model):
    first_name = models.CharField(max_length=20)
    secound_name = models.CharField(max_length=20)
    # id = models.No
    Email = models.CharField(max_length=50)
    date_join = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

