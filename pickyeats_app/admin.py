from django.contrib import admin

from .models import User, Party, LikedRestaurant, MatchedRestaurant

# Register your models here.
admin.site.register(User)
admin.site.register(Party)
admin.site.register(LikedRestaurant)
admin.site.register(MatchedRestaurant)