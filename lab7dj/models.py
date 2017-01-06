from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.IntegerField(default= 0 )
    phone = models.CharField(max_length=15, default='')
    is_in_black_list = models.BooleanField(default= 0)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class ante_model (models.Model):
    amount = models.FloatField()
    user_for = models.ForeignKey(User, null=True)
    team_for = models.ForeignKey("team_model", null=True)
    def __str__(self):
        return str(self.amount)

class team_model (models.Model):
    name = models.CharField(max_length=255, unique=True)
    kind_of_sport = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    quantity_win = models.IntegerField(default=0)
    quantity_lose = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)