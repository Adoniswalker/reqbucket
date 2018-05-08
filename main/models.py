import uuid

from django.contrib.auth.models import User
from django.db import models
import short_url


class EndPoint(models.Model):
    url_end = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    whos = models.ForeignKey(User, on_delete=models.CASCADE, related_name='endpoints')
    url_name = models.CharField(max_length=20, null=True)
    date_insert = models.DateTimeField(auto_now_add=True, editable=False)
    json_response = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return str(short_url.encode_url(self.id))

    class Meta:
        ordering = ['-date_insert']


class RequestDeport(models.Model):
    end_point = models.ForeignKey(EndPoint, on_delete=models.CASCADE, related_name='requests')
    method = models.CharField(max_length=20, default='get')
    content_type = models.CharField(max_length=100)
    content_length = models.IntegerField(null=True)
    remote_address = models.CharField(max_length=30, null=True)
    http_user_agent = models.CharField(max_length=256, null=True)
    body = models.CharField(max_length=256, null=True)
    content_params = models.CharField(max_length=100, null=True)
    COOKIES = models.TextField(null=True)
    date_insert = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.end_point)

    def save(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        super(RequestDeport, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_insert']
