from rest_framework.test import APITestCase
from rest_framework import status
from product.models import Product
from vendor.models import Vendor
from vendor_product_mapping.models import VendorProductMapping


class ProductAPITest(APITestCase):

    def test_create_product(self):
        url = "/api/products/"
        data = {
            "name": "Azure Cloud",
            "code": "AZURE",
            "description": "Microsoft Azure Cloud Platform"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_product_list(self):
        Product.objects.create(
            name="AWS",
            code="AWS",
            description="Amazon Web Services"
        )
        url = "/api/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        product = Product.objects.create(
            name="GCP",
            code="GCP",
            description="Google Cloud Platform"
        )
        url = f"/api/products/{product.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "GCP")

    def test_update_product(self):
        product = Product.objects.create(
            name="Test Product",
            code="TEST",
            description="Test Description"
        )
        url = f"/api/products/{product.id}/"
        data = {
            "name": "Updated Product",
            "code": "TEST",
            "description": "Updated Description"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, "Updated Product")

    def test_delete_product(self):
        product = Product.objects.create(
            name="Delete Test",
            code="DEL",
            description="To be deleted"
        )
        url = f"/api/products/{product.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_filter_products_by_vendor(self):
        # Create test data
        vendor = Vendor.objects.create(
            name="Microsoft",
            code="MS",
            description="Software Vendor"
        )
        product1 = Product.objects.create(
            name="Azure",
            code="AZURE",
            description="Cloud Platform"
        )
        product2 = Product.objects.create(
            name="Office 365",
            code="O365",
            description="Productivity Suite"
        )
        # Create mapping between vendor and product1
        VendorProductMapping.objects.create(vendor=vendor, product=product1)

        # Test filtering by vendor_id=1 (vendor.id should be 1)
        response = self.client.get("/api/products/?vendor_id=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return only product1
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Azure")