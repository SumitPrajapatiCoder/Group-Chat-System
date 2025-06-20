"""
URL configuration for group_chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path,include
from chat import views as chat_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_views.index, name='home'),
    path('register/', chat_views.register_view, name='register'),
    path('accounts/login/', chat_views.login_view, name='login'),
    path('logout/', chat_views.logout_view, name='logout'),
    path('messages/', chat_views.get_messages, name='get_messages'),
    path('clear-messages/', chat_views.clear_messages, name='clear_messages'),
    path('edit-message/<int:message_id>/', chat_views.edit_message, name='edit_message'),
    path('room/', chat_views.room, name='room'),
    path('', include('chat.urls')),
    path('back/', chat_views.back, name='back'),
] 

