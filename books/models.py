from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name



class Product(models.Model):
    name = models.CharField(max_length=64, blank=False, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    discount = models.IntegerField(default=0, blank=True)
    author = models.CharField(max_length=64, blank=False, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=False, null=True, default=None)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media2/products_images/', blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

class Http(models.Model):
    http_info = models.CharField(max_length=64, blank=False, null=True)

