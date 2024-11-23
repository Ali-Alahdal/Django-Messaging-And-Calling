from django.shortcuts import render
from rest_framework import generics , status 
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ChatSerializer 
from .models import Chats
import uuid
# Create your views here.



class ChatsView(APIView):

    def post(self , request):

        serializer =  ChatSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getChat(request):
    # chats = Chats.objects.filter(user_1 = request.user)

    return Response({"Shill" : "djiwadja"})
        