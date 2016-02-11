from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^get_end/$',views.CreateEndPoint.as_view(), name = 'create_end' ),
    url(r'^(?P<end_point>[a-zA-Z0-9_]+)/$', csrf_exempt(views.MainView.as_view()), name='major'),
]