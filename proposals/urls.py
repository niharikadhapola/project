from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_new'),
    path('edit/<int:pk>/', views.post_update, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('index/', include(('user_accounts.urls', 'user_accounts'), namespace='index')),
    path("by/join/<int:pk>/",views.SingleGroup.as_view(),name="post_join"),
    path("join/<int:pk>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<int:pk>/",views.LeaveGroup.as_view(),name="leave"),
    path("userpost/",views.UserPosts.as_view(),name="for_user"),

]