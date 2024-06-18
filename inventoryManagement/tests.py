from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item, Supplier

class SupplierTests(APITestCase):
  # create 2 users that will be used for testing data modification later
  def setUp(self):
    self.supplier1 = Supplier.objects.create(name='Priority Soft', email='hr@prioritySoft.rs', address='Serbia', phone_number='1234567890')
    self.supplier2 = Supplier.objects.create(name='Anastasia', email='ana@prioritySoft.rs', address='Kenya', phone_number='0987654321')


  def test_create_supplier(self):
    # we will need the endpoint URL
    url = reverse('supplier-list')
    data = {
      "name": "Chiemezuo",
      "email": "chiemezuoakujobi@gmail.com",
      "address": "Somewhere in Abuja",
      "phone_number": "09012345678"
    }
    
    # mimic hitting post URL with payload & keep response for comparison
    response = self.client.post(url, data, format='json')
    
    # Should be 3 because 2 were created in setup
    self.assertEqual(Supplier.objects.count(), 3)
    
    # Successful post should return 201 status
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
  def test_get_supplier_by_id(self):
    # Retrieve first supplier
    url = reverse('supplier-detail', kwargs={'pk': self.supplier1.pk})
    response = self.client.get(url, format='json')
    
    # Fetch should return 200 status
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], self.supplier1.name)
    
    
  def test_update_supplier(self):
    url = reverse('supplier-detail', kwargs={'pk': self.supplier1.pk})
    
    # New data for patch method
    data = {
      "name": "Priority.rs",
      "email": "different.email@email.com",
    }
    
    response = self.client.patch(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Check new value from DB
    self.supplier1.refresh_from_db()
    
    self.assertEqual(self.supplier1.name, "Priority.rs")
    # Testing that old email is not kept
    self.assertNotEqual(self.supplier1.email, "hr@prioritySoft.rs")
    
    
  def test_delete_supplier(self):
    url = reverse('supplier-detail', kwargs={'pk': self.supplier1.pk})
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Supplier.objects.count(), 1)
    
  
  def test_get_all_suppliers(self):
    url = reverse('supplier-list')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]['name'], self.supplier1.name)
    self.assertEqual(response.data[1]['name'], self.supplier2.name)
    
    
class ItemTests(APITestCase):
  def setUp(self):
    # Create supplier that will be attached to item.
    self.supplier1 = Supplier.objects.create(name='Priority Soft', email='hr@prioritySoft.rs', address='Serbia', phone_number='1234567890')
    self.item1 = Item.objects.create(name="Code", description="Interview code 1", price=10.0)
    self.item1.suppliers.add(self.supplier1)
    
  def test_create_item(self):
    url = reverse('item-list')
    data = {
      "name": "Dell Laptops",
      "description": "Portable computing devices",
      "price": 20.0,
      "suppliers": [self.supplier1.pk]
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Item.objects.count(), 2) # Including item from setup
    # Count the suppliers
    self.assertEqual(Item.objects.get(name="Dell Laptops").suppliers.count(), 1)
    
  
  def test_get_item_by_id(self):
    url = reverse('item-detail', kwargs={'pk': self.item1.pk})
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], self.item1.name)
    
    
  def test_update_item(self):
    url = reverse('item-detail', kwargs={'pk': self.item1.pk})
    data = {
      "name": "books",
    }
    
    response = self.client.patch(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.item1.refresh_from_db()
    self.assertEqual(self.item1.name, "books")


  def test_delete_item(self):
    url = reverse('item-detail', kwargs={'pk': self.item1.pk})
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Item.objects.count(), 0)
    
    
  def test_add_suppliers_to_item(self):
    supplier2 = Supplier.objects.create(name="Mezuo", email="mezuo@example.com", address="home", phone_number="0987654321")
    url = reverse('item-detail', kwargs={'pk': self.item1.pk})
    data = {
      "name": self.item1.name,
      "description": self.item1.description,
      "price": self.item1.price,
      "suppliers": [self.supplier1.pk, supplier2.pk]
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.item1.refresh_from_db()
    self.assertEqual(self.item1.suppliers.count(), 2)
    
    
  def test_get_all_items(self):
    url = reverse('item-list')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['name'], self.item1.name)