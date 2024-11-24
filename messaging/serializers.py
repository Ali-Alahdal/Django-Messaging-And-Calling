from rest_framework import serializers
from .models import Chats




class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['username_1' , 'username_2']

    def create(self , data):
        newChat = Chats.objects.create(user_1 = data["user_1"] , user_2 = data["user_2"])
        newChat.save()
        return newChat

   
      
