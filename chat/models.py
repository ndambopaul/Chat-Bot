from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=255, default="user")
    content = models.CharField(max_length=500)
    response = models.TextField(null=True)
    timestamp = models.DateField(auto_now_add=True)