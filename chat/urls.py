from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('messages/', views.get_messages, name='get_messages'),
    path('list-users-json/', views.list_users_json, name='list_users_json'),
    path('toggle-block-user/<int:user_id>/', views.toggle_block_user, name='toggle_block_user'),
]
