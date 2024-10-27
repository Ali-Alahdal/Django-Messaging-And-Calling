from rest_framework import serializers
from .models import CustomUser
import bcrypt


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username' , "password" , "email"]


    def create(self , validated_data):

        password = validated_data["password"]
        hashed_password = self.hashing_password(password)

        newUser = CustomUser()
        newUser.username = validated_data["username"]
        newUser.password = hashed_password
        newUser.email = validated_data["email"]
        newUser.save()

        return newUser

    def hashing_password(self, password):
        salted = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"),salted)
        return hashed.decode("utf-8")