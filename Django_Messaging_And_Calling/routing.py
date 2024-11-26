from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from messaging.consumers import BroadcastConsumer

application = ProtocolTypeRouter({
   
    "websocket": URLRouter([
        path("ws/chat/", BroadcastConsumer.as_asgi())
        
    ])
    
})