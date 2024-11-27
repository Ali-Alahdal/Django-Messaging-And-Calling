from rest_framework import serializers
from .models import Chats , Messages
from users.serializers import UserSerializer



class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chats
        fields = ['participants','created_at']

    def create(self , data ):
        
        newChat = Chats.objects.create()
        newChat.participants.set(data["participants"])
        newChat.save() 
        return newChat

   
      
class MessageSerializer(serializers.ModelSerializer):

    
    sender_id = serializers.UUIDField(format='hex')

    class Meta:
        model = Messages
        fields = ["content" , "sender_id", "sent_time" , "chat"]
      

    