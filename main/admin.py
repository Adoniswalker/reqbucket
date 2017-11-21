from django.contrib import admin

from django.contrib import admin

from .models import EndPoint, RequestDeport


class EndpointAdmin(admin.ModelAdmin):
    fields = ['url_name', 'whos', 'date_insert']


admin.site.register(RequestDeport)
admin.site.register(EndPoint, EndpointAdmin)
