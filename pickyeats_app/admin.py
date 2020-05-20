from django.contrib import admin

from .models import User, Party, LikedRestaurant

# Register your models here.
admin.site.register(User)
admin.site.register(Party)
admin.site.register(LikedRestaurant)