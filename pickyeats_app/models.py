from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class Party(models.Model):
    title = models.CharField(max_length=30)
    search_query = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

class User(AbstractUser):
    name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=10, default='')
    active_party = models.ForeignKey(Party, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}: {self.name}'

class LikedRestaurant(models.Model):
    name = models.CharField(max_length=50)
    yelp_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)