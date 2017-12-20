"""reqbucket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from main import views as mainviews
from accounts import views as account_views

# app_name = 'ajax_url'
# xhttps_urls = [
    # url(r'^url_data/(?P<end_id>\d+)', account_views.url_data, name='url_data'),
    # url()
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='home'),
    url(r'^contact/', mainviews.contact_view, name='contact'),
    url(r'^about/', TemplateView.as_view(template_name='main/about.html'), name='about'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^jb/', include('main.urls')),
    url(r'^dashboard/', account_views.DashBoard.as_view(), name='dashboard'),
    url(r'^dash/(?P<end_point>\w+)/', account_views.DashboardFuc.as_view(), name='dashboardkey'),
    url(r'^ajax_url/url_data/(?P<end_id>\d+)',account_views.url_data, name='url_data' ),
    # url(r'^ajax_url/url_data/(?P<end_id>\d+)', include(xhttps_urls, namespace='ajax_url')),
]
