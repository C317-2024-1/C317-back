from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^register/$', views.register),
    re_path(r'^login/$', views.login),
    re_path(r'^user/$', views.user),
    re_path(r'^logout/$', views.logout),
    re_path(r'^message/$', views.message_handler),
    #re_path(r'^api/user/(?P<pk>[0-9]+)$', views.user),
 #   re_path(r'^api/user/(?P<pk>[0-9]+)/messages$', views.user_messages),
]