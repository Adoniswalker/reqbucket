from django.contrib.auth.models import User
from django.db import models
import short_url


class EndPoint(models.Model):
    whos = models.ForeignKey(User, on_delete=models.CASCADE, related_name='endpoints')
    url_name = models.CharField(max_length=20, null=True)
    date_insert = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        # return str(self.whos)+str(self.id)
        return str(short_url.encode_url(self.id))

    class Meta:
        ordering = ['date_insert']


class RequestDeport(models.Model):
    end_point = models.ForeignKey(EndPoint, on_delete=models.CASCADE, related_name='request_data')
    method = models.CharField(max_length=20, default='get')
    content_type = models.CharField(max_length=100)
    content_length = models.IntegerField(null=True)
    remote_address = models.CharField(max_length=30, null=True)
    http_user_agent = models.CharField(max_length=256, null=True)
    body = models.CharField(max_length=256, null=True)
    content_params = models.CharField(max_length=100, null=True)
    COOKIES = models.CharField(max_length=100, null=True)
    date_insert = models.DateTimeField(auto_now=True)
    # encoding = models.CharField(max_length=10)
    # meta_header = models.CharField(max_length=255, default='nothing')

    def __str__(self):
        return str(self.end_point)
