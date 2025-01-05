
from channels.consumer import SyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync


from .models import Chats
from users.models import CustomUser 
from .serializers import MessageSerializer 
from users.serializers import SearchUserSerializer
import json



class CallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "call_room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Broadcast data to the group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'call_message',
                'message': data,
            }
        )

    async def call_message(self, event):
        await self.send(text_data=json.dumps(event['message']))
   
        


# class CallConsumer(SyncConsumer):
#     def websocket_connect(self , event):
#         chat_id =  self.scope['url_route']['kwargs']['chat_id']
#         self.room_name = str(chat_id)
#         self.send({"type": "websocket.accept"})
#         async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
#         print("connected" ,  self.room_name)


#     def websocket_receive(self, text_data):
#         # data = json.loads(text_data)
#         self.channel_layer.group_send(
#             "webrtc_group",
#             {
#                 "type": "signal_message",
#                 "message": text_data
#             }
#         )

#     def signal_message(self, event):
#          self.send(text_data=json.dumps(event["message"]))

#     def websocket_disconnect(self, event):
#         async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
#         print("disconnected")


class SearchConsumer(SyncConsumer):
    def websocket_connect(self, event):
       
        current_user = self.scope['cookies']['user_id']
        self.room_name = str(current_user )
        self.send({"type": "websocket.accept"})

        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)

    def websocket_receive(self, event):

        if event.get("text") is not None and event.get("text") != "" :
            users = CustomUser.objects.filter(username__icontains=event.get("text"))

            serializer = SearchUserSerializer(users , many=True)
       
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    "type": "websocket.message",
                    "text": json.dumps(serializer.data[:10])
                }
            )
        else : 
            async_to_sync(self.channel_layer.group_send)(
                    self.room_name,
                    {
                        "type": "websocket.message",
                        "text": json.dumps([])
                    }
                )
        

    def websocket_message(self, event):
      
        self.send({

            "type": "websocket.send", 
            "text": event.get("text")

            })
       

    def websocket_disconnect(self, event):

        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
     
   



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
            "text" : json.dumps(serializer.data) 

        })
      
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
     
    
    def websocket_receive(self , event):
        currentUser  =  self.scope['cookies']['user_id']
       
        newMessage = MessageSerializer(data= {'content' : event.get('text'), "sender_id" :currentUser , "chat" : int(self.room_name)  })
       
        if newMessage.is_valid():
            newMessage.save()
            current_chat = Chats.objects.get(pk = self.room_name)
            messsages = current_chat.chat_messages.all()

            serializer = MessageSerializer(messsages, many=True)
            async_to_sync(self.channel_layer.group_send)(self.room_name ,{
                "type" : "websocket.message",
                "text" :  json.dumps( serializer.data) 
            })
            raise StopConsumer()
        


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






