from django.contrib import admin

from .models import AppUser, Party, LikedRestaurant

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Party)
admin.site.register(LikedRestaurant)