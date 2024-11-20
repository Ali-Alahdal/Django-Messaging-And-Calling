from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ChatsView  


urlpatterns = [
    path("createChat/" , ChatsView.as_view() , name="create_chat"),
    path("getChats/<uuid:id>/" , ChatsView.as_view() ,name="get_chats" )
]
