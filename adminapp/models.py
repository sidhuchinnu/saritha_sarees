from django.db import models

# Create your models here.
class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    

    class Products(models.Model):
        name = models.CharField(max_length=200)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.IntegerField()
        image = models.ImageField(upload_to='product_images/', blank=True, null=True)

        def __str__(self):
            return self.name

