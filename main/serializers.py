from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import EndPoint, RequestDeport


class EndpointSerializer(serializers.HyperlinkedModelSerializer):
    whos=serializers.ReadOnlyField(source='whos.id')
    requests = serializers.HyperlinkedRelatedField(many=True, view_name='requestdeport-detail', read_only=True)
    date_insert = serializers.ReadOnlyField()

    class Meta:
        model = EndPoint
        fields = ('id', 'whos', 'url_name', 'date_insert', 'json_response', 'requests')


class RequestDeportSerializer(serializers.HyperlinkedModelSerializer):
    end_point = serializers.ReadOnlyField(source='end_point.end_point_id')

    class Meta:
        model = RequestDeport
        fields = ('end_point', 'method', 'content_type', 'remote_address', 'http_user_agent', 'body', 'date_insert')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    endpoints = serializers.HyperlinkedRelatedField(many=True, view_name='endpoint-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'endpoints')
        read_only_fields = ('id', 'username', 'email')
