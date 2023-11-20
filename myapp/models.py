from django.db import models

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',blank=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
# Create your models here.



