from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^exists$', views.exists),
    url(r'^create$', views.create),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
]
