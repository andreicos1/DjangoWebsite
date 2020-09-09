from django.urls import path
from . import views

app_name='topics'

urlpatterns = [
    path('', views.TopicList.as_view(), name='index'),
    path('<slug:slug>/', views.TopicDetail.as_view(), name='detail'),
    path('<slug:slug>/posts', views.PostsInTopicDetail.as_view(), name='list_of_posts'),
]
