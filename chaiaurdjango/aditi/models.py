from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
    ( 'ML','MASALA'),
    ( 'GR','GINGER'),
    ( 'KL','KIWI'),
    ( 'PL','PLAIN'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=None, upload_to='chais/')
    date_time = models.DateTimeField(default=timezone.now)
    type = models.CharField(choices=CHAI_TYPE_CHOICE, max_length=2)


    def __str__(self):
        return self.name
