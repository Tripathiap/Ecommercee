from django.urls import path, include
from . import views


urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_view/', views.logout_view, name='logout'),
    path('register_user/', views.register_user, name='register'),
]
