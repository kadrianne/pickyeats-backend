from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Party, LikedRestaurant
from .serializers import UserSerializer, PartySerializer, LikedRestaurantSerializer

# Create your views here.
class PartyView(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LikedRestaurantView(viewsets.ModelViewSet):
    queryset = LikedRestaurant.objects.all()
    serializer_class = LikedRestaurantSerializer

