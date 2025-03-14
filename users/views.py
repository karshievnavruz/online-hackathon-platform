from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
