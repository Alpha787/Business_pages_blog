from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.IntegerField('Num of post', default=0)
    date = models.DateTimeField('Date posted', default=timezone.now)
    text = models.TextField()