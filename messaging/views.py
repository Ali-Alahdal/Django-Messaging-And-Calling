from django.shortcuts import render
from rest_framework import generics , status 
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ChatSerializer 
from users.models import CustomUser
from .models import Chats
from django.http import JsonResponse
import uuid
# Create your views here.



class ChatsView(APIView):

    def post(self , request):

        
        participants = request.data["participants"]
        participants.append( request.COOKIES.get("user_id"))
        serializer =  ChatSerializer(data={"participants" : participants} )
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChat(request):

    try: 
       
        chats =  request.user.chats.all()
        chats_data = []
        for chat in chats:    
            chats_data.append(
                {
                    'chat_id': chat.id,
                    'chat_name': [user.username  for user in chat.participants.exclude(id = request.user.id)],
                    'chatUser_id' : [user.id  for user in chat.participants.exclude(id = request.user.id)]
                }
            )
                
        return Response( chats_data)
    
    except:
        return Response({"success" : False})
    
        