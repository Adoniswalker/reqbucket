from django.contrib.auth.models import User
from django.db import models


class EndPoint(models.Model):
    whos = models.ForeignKey(User,on_delete=models.CASCADE)
    date_insert = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.whos)+str(self.id)


class RequestDeport(models.Model):
    end_point = models.ForeignKey(EndPoint, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=100)
    body = models.CharField(max_length=256)
    content_params =models.CharField(max_length=100)
    encoding = models.CharField(max_length=10)
    COOKIES = models.CharField(max_length=100)
    date_insert = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.end_point)