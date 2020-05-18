from rest_framework import serializers

from .models import AppUser, Party, LikedRestaurant

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'user', 'name', 'phone', 'email', 'active_party')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'title', 'created_at')

class LikedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedRestaurant
        fields = ('id', 'name', 'yelp_id', 'party', 'user')