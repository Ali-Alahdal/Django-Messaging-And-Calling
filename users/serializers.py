from rest_framework import serializers

from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name' ,'username' , "password" , "email" ]

    def create(self , validated_data):

        #Hashing password with bcrypt using default settings for hashing
        hashed_password = make_password(validated_data["password"])

        newUser = CustomUser()
        newUser.first_name = validated_data["first_name"]
        newUser.last_name = validated_data["last_name"]
        newUser.username = validated_data["username"]
        newUser.email = validated_data["email"]
        newUser.password = hashed_password

        newUser.save()

        return newUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(f"Invalid username or password ")
        
        data['user'] = user
        return data

 