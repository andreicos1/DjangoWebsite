from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.post_detail, name='detail'),
    path('<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
