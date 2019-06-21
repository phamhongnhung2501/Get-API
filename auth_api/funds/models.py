from django.db import models
from users.models import User
from datetime import datetime  
 
 
class Fund(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user_story = models.CharField(max_length=500, null=True)
    user_task = models.CharField(max_length=500, null=True)
    content =  models.CharField(max_length=140, default=' ')
    expenses = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    user = models.ForeignKey('users.User', related_name='funds', on_delete=models.CASCADE, null=False)
 
    class Meta:
        ordering = ('created',)