from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.AppUserView)
router.register('liked-restaurants', views.LikedRestaurantView)
router.register('parties', views.PartyView)

urlpatterns = [
    path('', include(router.urls))
]