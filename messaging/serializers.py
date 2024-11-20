from rest_framework import serializers
from .models import Chats


class CreateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['user_1' , 'user_2']

    def create(self , data):
        newChat = Chats.objects.create(user_1 = data["user_1"] , user_2 = data["user_2"])
        newChat.save()
        return newChat
    

class GetChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['user_1' , 'user_2' , 'username_1' , 'username_2']