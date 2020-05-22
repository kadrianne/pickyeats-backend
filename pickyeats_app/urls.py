from django.urls import path, include
from . import views
from rest_framework import routers
from .api import SignupAPI, LoginAPI, FriendSearchAPI, PartyRestaurantsAPI, MatchedRestaurantsAPI

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('liked-restaurants', views.LikedRestaurantView)
router.register('matched-restaurants', views.MatchedRestaurantView)
router.register('parties', views.PartyView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth', include('knox.urls')),
    path('api/auth/signup', SignupAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/users', FriendSearchAPI.as_view()),
    path('api/party-restaurants', PartyRestaurantsAPI.as_view()),
    path('api/matched-restaurants', MatchedRestaurantsAPI.as_view())
]