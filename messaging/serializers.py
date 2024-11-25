from rest_framework import serializers
from .models import Chats




class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chats
        fields = ['participants','created_at' ]

    def create(self , data ):
        
        newChat = Chats.objects.create()
        newChat.participants.set(data["participants"])
        newChat.save() 
        return newChat

   
      
