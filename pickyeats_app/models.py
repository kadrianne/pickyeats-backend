from django.db import models

# Create your models here.
class Party(models.Model):
    title = models.CharField(max_length=30)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    active_party = models.ForeignKey(Party, blank=True, null=True, on_delete=models.SET_NULL)

class LikedRestaurant(models.Model):
    name = models.CharField(max_length=50)
    yelp_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)