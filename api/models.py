from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    msg = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.msg
    