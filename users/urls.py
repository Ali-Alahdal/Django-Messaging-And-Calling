from django.urls import path
from .views import RegisterView  , CustomTokenObtainPairView , CustomTokenRefreshView , logout
from  rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path("register/" , RegisterView.as_view() , name="register"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('logout/' , logout , name="logout" )
]
