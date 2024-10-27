from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ViewTest

router = DefaultRouter()
router.register(r"api", ViewTest)



urlpatterns = [
    path("" , include(router.urls)),
    
]
