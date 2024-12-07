from django.urls import path
from .views import RegisterView  , CustomTokenObtainPairView , CustomTokenRefreshView , logout , get_profile
from  rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path("register/" , RegisterView.as_view() , name="register"),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='refresh_token'),
    path('getProfile/', get_profile, name='get_profile'),
    path('logout/' , logout , name="logout" )
]
