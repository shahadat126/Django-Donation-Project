from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Donation(models.Model):
    name= models.CharField(max_length=100)
    amount = models.IntegerField()
    photo = models.ImageField(upload_to="App/photo")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE )
    def __str__(self):
        return f"{self.name}"