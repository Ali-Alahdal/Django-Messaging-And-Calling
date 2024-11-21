from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import UserSerializer 
from .models import CustomUser
import jwt,datetime , json
class RegisterView(APIView):
    def post(self , request):
        serializer = UserSerializer(data =request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self , request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not Found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        
       
        payload = {
            "id" :  str(user.id) ,
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            "iat" : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload , "dwajhgfiow4236h96ygt++_987dawy221/vadw]/.,jdwahgfywfy91482088" , algorithm="HS256")
        response = Response()

    

        response.set_cookie(key="jwt" , value=token , httponly = True)

        return response
        

