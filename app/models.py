from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Review(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return f'{self.title} by {self.author}'