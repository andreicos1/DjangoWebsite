from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserList.as_view(), name ='users_list'),
    path('<int:pk>/profile', views.UserDetail.as_view()
                            ,name = 'profile'),
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                            redirect_authenticated_user=True),
                            name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html')
                            ,name='logout'),
    path('<int:pk>/comments/',views.UserDetail.as_view(template_name='users/comments.html')
                            ,name='comments'),
    path('update_profile/', views.update_profile, name='update_profile'),

]
