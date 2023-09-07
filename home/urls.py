
from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home' ),
     path("signup", views.SignUpView.as_view() , name='signup' ),
    path("login", views.LoginInterfaceView.as_view() , name='login' ),
    path("logout", views.LogoutInterfaceView.as_view() , name='logout' ),
]