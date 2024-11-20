from django.shortcuts import render
from rest_framework import generics , status 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateChatSerializer , GetChatsSerializer
from .models import Chats
import uuid
# Create your views here.


class ChatsView(APIView):
    
    def get(self , request , id):
        chats = Chats.objects.filter(user_1 = id)
        serializer = GetChatsSerializer(chats, many=True)
        
        return Response(
             serializer.data
            )

    def post(self , request):
        serializer =  CreateChatSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
# class GetChatsView(viewsets.ModelViewSet):
#     queryset = Chats.objects.filter()
#     serializer_class = GetChatsSerializer
