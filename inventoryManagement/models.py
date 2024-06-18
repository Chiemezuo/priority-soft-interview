from django.db import models

class Supplier(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateField(auto_now_add=True)
  suppliers = models.ManyToManyField(Supplier, related_name='items')
  
  def __str__(self):
    return self.name