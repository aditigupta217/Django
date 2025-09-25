from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photos = models.ImageField( upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    