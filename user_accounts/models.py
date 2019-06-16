from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    INDIVIDUAL = 'Individual'
    COMPANY = 'Company'
    CHOICES = (
        (INDIVIDUAL, 'Individual'), 
        (COMPANY, 'Company'),
        )
    category= models.CharField(max_length=100,choices=CHOICES,default='Individual')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username