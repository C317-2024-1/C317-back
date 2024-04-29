from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'users/$', views.user_list),
    re_path(r'^register/$', views.register),
    re_path(r'^login/$', views.login),
    #re_path(r'^api/user/(?P<pk>[0-9]+)$', views.user),
 #   re_path(r'^api/user/(?P<pk>[0-9]+)/messages$', views.user_messages),
]