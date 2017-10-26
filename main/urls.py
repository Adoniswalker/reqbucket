from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_end/$',views.get_end_view, name = 'get_end' ),
    url(r'^(?P<id>[0-9]+)/$', views.MainView.as_view(), name='major'),
]