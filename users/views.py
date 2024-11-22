from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import UserSerializer , TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
    



class RegisterView(APIView):
    def post(self , request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
    def post(self , request  , *args, **kwargs):

        try:
            res = super().post(request , *args, **kwargs)
            tokens = res.data

            response = Response()

            response.data = {
                "success" : True
            }
                
            response.set_cookie(
                key = "access_token",
                value = tokens["access"],
                httponly = True,
                secure = True

            )

            response.set_cookie(
                key = "refresh_token",
                value = tokens["refresh"],
                httponly = True,
                secure = True
            )

            return response
        
        except :
          
          return Response({"success" : False})