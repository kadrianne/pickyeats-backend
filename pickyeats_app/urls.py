from django.urls import path, include
from . import views
from rest_framework import routers
from .api import SignupAPI, LoginAPI

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('app-users', views.AppUserView)
router.register('liked-restaurants', views.LikedRestaurantView)
router.register('parties', views.PartyView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth', include('knox.urls')),
    path('api/auth/signup', SignupAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view())
]