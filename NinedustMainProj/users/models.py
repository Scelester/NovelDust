from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class extra_user_info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/px/%Y-%m')
    address = models.CharField(max_length=200)