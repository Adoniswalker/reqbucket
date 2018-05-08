from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from main import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'requestdeport', views.RequestDeportViewSet)
router.register(r'endpoint', views.EndPointViewSet, base_name='endpoint')
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [
    url(r'^', include(router.urls))
]
