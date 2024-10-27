from rest_framework import serializers
from .models import Test_1


class Test_Serializer(serializers.ModelSerializer):
    class Meta:
      model = Test_1
      fields = ['id' , 'msg' ,'sender','receiver']