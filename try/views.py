from django.shortcuts import render
from django.http import HttpResponse
from .models import Test_1
from rest_framework import viewsets
from .serializers import Test_Serializer

def hello(request):

    newT = Test_1.objects.first()
    # newT.sender = "Hello"
    # newT.receiver = "World,"
    # newT.msg = "Borther what'up"
    # newT.save()
    # tests =  str( Test_1.objects.first().msg)

    return HttpResponse("Hello World ," + newT.msg)



class ViewTest(viewsets.ModelViewSet):
    queryset = Test_1.objects.all()
    serializer_class = Test_Serializer
    