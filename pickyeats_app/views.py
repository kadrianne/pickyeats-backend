from django.shortcuts import render

from rest_framework import viewsets
from .models import AppUser, Party, LikedRestaurant
from .serializers import AppUserSerializer, PartySerializer, LikedRestaurantSerializer

# Create your views here.
class PartyView(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class AppUserView(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class LikedRestaurantView(viewsets.ModelViewSet):
    queryset = LikedRestaurant.objects.all()
    serializer_class = LikedRestaurantSerializer

