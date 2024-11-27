
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

from .models import Chats
from .serializers import MessageSerializer
import json


class OneConsumer(SyncConsumer):
    def websocket_connect(self, event):

        chat_id =  self.scope['url_route']['kwargs']['chat_id']
        self.room_name = str(chat_id)

        current_chat = Chats.objects.get(pk = chat_id)

        messsages = current_chat.chat_messages.all()

        serializer = MessageSerializer(messsages, many=True)

        self.send({
            "type":"websocket.accept",
        })
        self.send({
            "type" : "websocket.send",
            "text" : json.dumps({"messages" : serializer.data}) 

        })
      
        print(f"Server: Connection Accepted , {serializer.data} , ")
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
     
    
    def websocket_receive(self , event):
        currentUser  =  self.scope['cookies']['user_id']
        newMessage = MessageSerializer(data= {'content' : event.get('text'), "sender_id" :currentUser , "chat" : int(self.room_name)  })
        if newMessage.is_valid():
            newMessage.save()
            async_to_sync(self.channel_layer.group_send)(self.room_name ,{
                "type" : "websocket.message",
                "text" :  json.dumps( newMessage.data) 
            })

        # async_to_sync(self.channel_layer.group_send)(self.room_name ,{
        #         "type" : "websocket.message",
        #         "text" :  "Skijnt"
        #     })
    
    def websocket_message(self , event):
        self.send({
            "type" : "websocket.send",
            "text" : event.get("text")
        })

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
        print("Server: Connection Closed")



class BroadcastConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.room_name = "broadcast"
        self.send({
            "type":"websocket.accept"
            })
        print("Server: Connection Accepted")
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
    
    def websocket_receive(self , event):
        
        async_to_sync(self.channel_layer.group_send)(self.room_name ,{
            "type" : "websocket.message",
            "text" : event.get("text")
        })
    
    def websocket_message(self , event):
        self.send({
            "type" : "websocket.send",
            "text" : event.get("text")
        })

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
        print("Server: Connection Closed")

