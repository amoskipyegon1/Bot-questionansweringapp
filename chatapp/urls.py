from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
    path('chat', views.chat, name='index'),
    path('signin', views.signin, name='signin'),
    path('login', LoginView.as_view(template_name='chatapp/login.html'),name='login'),
    path('', views.home, name='home'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('chatreply', views.response, name='chatreply'),
]
