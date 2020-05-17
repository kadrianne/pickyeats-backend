from rest_framework import serializers

from .models import User, Party, LikedRestaurant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'email', 'active_party')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'title', 'created_at')

class LikedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedRestaurant
        fields = ('id', 'name', 'yelp_id', 'party', 'user')