from django.urls import re_path
from django_simple_forum import views

urlpatterns = [
    re_path(r'^$', views.index, name='forum-index'),
    re_path(r'^(\d+)/$', views.forum, name='forum-detail'),
    re_path(r'^topic/(\d+)/$', views.topic, name='topic-detail'),
    re_path(r'^reply/(\d+)/$', views.post_reply, name='reply'),
    re_path(r'newtopic/(\d+)/$', views.new_topic, name='new-topic'),
]