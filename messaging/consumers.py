
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync



from threading import Timer

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

