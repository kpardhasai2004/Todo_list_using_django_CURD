from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True, )
    work = models.CharField(max_length=100000000000000000000)
    
    
    