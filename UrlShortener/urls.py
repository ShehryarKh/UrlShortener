	
from django.conf.urls import url
from django.contrib import admin
from UrlShortener import views
from UrlShortener.views import UrlView


urlpatterns = [

url(r'^$', UrlView.as_view(), name="index"),


url(r'^(?P<shortened>[0-9A-Za-z\-]+)$', UrlView.as_view(), name="index"),

]


