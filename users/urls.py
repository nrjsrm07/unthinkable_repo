
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hello.as_view(), name='hello'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('users/', views.Users.as_view(), name='users'),
    path('login/', views.Login.as_view(), name='login'),
    path('active_users/', views.OnlineUsers.as_view(), name='active_users'),
]
