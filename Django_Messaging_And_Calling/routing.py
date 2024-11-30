from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from messaging.consumers import  OneConsumer , SearchConsumer
from channels.sessions import SessionMiddlewareStack

from users.authentication import CustomAuthentication 
from django.core.asgi import get_asgi_application


application = ProtocolTypeRouter({


    "http" : get_asgi_application(),
    "websocket": SessionMiddlewareStack( 
        
        URLRouter([
        
            path("ws/search/" , SearchConsumer.as_asgi()),
            path("ws/chat/<int:chat_id>" , OneConsumer.as_asgi())
        
    ]))
    
})