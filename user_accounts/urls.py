from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='user_login'),
    path('complogin/', views.comp_login, name='user_login'),

]

