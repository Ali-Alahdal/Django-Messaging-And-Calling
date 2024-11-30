from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 



class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =  ['id' ,'first_name' , 'last_name' , 'email' , 'username' , 'password']
        
        extra_kwargs = {
            "password" : {"write_only" : True}
        }
        
    def create(self , validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance
    

class SearchUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id' , 'username']
