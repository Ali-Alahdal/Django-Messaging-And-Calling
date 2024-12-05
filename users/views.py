from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import UserSerializer , TokenObtainPairSerializer 
from rest_framework.decorators import api_view, permission_classes , authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny



class RegisterView(APIView):
    permission_classes = [AllowAny]
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
                "success" : True,
                "access_token" : tokens["access"]
                
            }
           
            response.set_cookie(
                key = "user_id",
                value = AccessToken(tokens['access']).get("user_id"),
                httponly = True,
                secure = True,
                samesite = "None",
                expires=datetime.utcnow() + timedelta(days=1), 
            )

            
            response.set_cookie(
                key = "access_token",
                value = tokens["access"],
                httponly = True,
                secure = True,
                samesite = "None",
                expires=datetime.utcnow() + timedelta(minutes=15),  
            )
            
            response.set_cookie(
                key = "refresh_token",
                value = tokens["refresh"],
                httponly = True,
                secure = True,
                samesite = "None",
                expires=datetime.utcnow() + timedelta(days=1),  
            )

            return response
        
        except :
          
          return Response({"success" : False , "status" : "Email or Password is not valid"})
        

class CustomTokenRefreshView(TokenRefreshView):
       
    def post(self , request  , *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        try:

            refresh_token = request.COOKIES.get("refresh_token")
            
            if refresh_token is None:
                raise AuthenticationFailed("Mdary")
                
            
            request.data["refresh"] = refresh_token
            res = super().post(request , *args, **kwargs)
            tokens = res.data

            response = Response()

            response.data = {
                "success" : True,
                "access_token" : tokens["access"]
            }
                
            response.set_cookie(
                key = "access_token",
                value = tokens["access"],
                httponly = True,
                secure = True,
                samesite = "None"
            )

            return response

        
        except : 
            return Response({"success" : False , "status" : "You are not logged in." })




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        resonse = Response()
        resonse.data = {
            'success' : True
        }

        resonse.delete_cookie("access_token", path="/" ,samesite = "None")
        resonse.delete_cookie("refresh_token" , path="/",samesite = "None")
        resonse.delete_cookie("user_id" , path="/",samesite = "None")

        return resonse
    except:

        return Response({
            'success' : False
        })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    