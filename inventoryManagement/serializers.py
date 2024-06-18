from rest_framework import serializers
from .models import Item, Supplier

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = ['id', 'name', 'email', 'address', 'phone_number', 'items']
    # we ideally want a depth of 1
    depth = 1
    
class ItemSerializer(serializers.ModelSerializer):
  suppliers = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True)
  
  class Meta:
    model = Item
    fields = ['id', 'name', 'description', 'price', 'created_at', 'suppliers']