from rest_framework import viewsets
from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  
class SupplierViewSet(viewsets.ModelViewSet):
  queryset = Supplier.objects.all()
  serializer_class = SupplierSerializer