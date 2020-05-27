from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Party, LikedRestaurant, MatchedRestaurant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'phone', 'active_party')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Email and/or password is incorrect')

class PartySerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Party
        fields = ('id', 'title', 'search_query', 'active', 'users', 'created_at')

class LikedRestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = LikedRestaurant
        fields = ('id', 'name', 'yelp_id', 'party', 'user', 'matched_restaurant')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'phone')

class MatchedRestaurantSerializer(serializers.ModelSerializer):
    liked_restaurants = LikedRestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = MatchedRestaurant
        fields = ('id', 'name', 'yelp_id', 'party', 'liked_restaurants')