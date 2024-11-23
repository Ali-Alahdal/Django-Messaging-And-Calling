from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ChatsView  , getChat


urlpatterns = [
    path("createChat/" , ChatsView.as_view() , name="create_chat"),
    path("getChats/" , getChat ,name="get_chats" ),
    
]
