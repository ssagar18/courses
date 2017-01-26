from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addnew$', views.addnew),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
]
