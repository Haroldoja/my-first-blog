#
# Created by HB Dec/20
#
from django.urls import re_path
from . import views
#
# using re_path as per https://docs.djangoproject.com/en/2.0/topics/http/urls/
#
urlpatterns = [
	re_path(r'^$', views.post_list, name='post_list'),
]
