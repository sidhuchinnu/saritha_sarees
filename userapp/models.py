from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    otp = models.CharField(max_length=10, blank=True, null=True)
    profile = models.FileField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name
    

