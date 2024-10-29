from rest_framework import serializer
from .models import Chats


class CreateChatSerializer(serializer.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['user_1' , 'user_2']

    def create(self , data):
        newChat = Chats.objects.create(user_1 = data["user_1"] , user_2 = data["user_2"])
        newChat.save()
        return newChat
    

class GetChatsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['user_1' , 'user_2']