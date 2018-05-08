from django.contrib import admin

from django.contrib import admin

from .models import EndPoint, RequestDeport


class EndpointAdmin(admin.ModelAdmin):
    list_display = ('id', 'whos', 'url_name', 'date_insert', 'url_end')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'end_point', 'method', 'content_type', 'remote_address')


admin.site.register(RequestDeport, RequestAdmin)
admin.site.register(EndPoint, EndpointAdmin)
