from django.conf.urls import url
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^category/(?P<pk>[\w-]+)/$', views.category, name="category"),
	url(r'^article/(?P<pk>\d+)/$', views.article, name='article'),
	url(r'^upload_image/$', views.upload_image, name = "upload_image"),
]