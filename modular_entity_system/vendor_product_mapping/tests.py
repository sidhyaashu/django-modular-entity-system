from rest_framework.test import APITestCase
from rest_framework import status

from vendor.models import Vendor
from product.models import Product


class VendorProductMappingTest(APITestCase):

    def setUp(self):

        self.vendor = Vendor.objects.create(
            name="Microsoft",
            code="MS",
            description="Vendor"
        )

        self.product = Product.objects.create(
            name="Azure",
            code="AZ",
            description="Cloud"
        )

    def test_create_mapping(self):

        url = "/api/vendor-product-mappings/"

        data = {
            "vendor": self.vendor.id,
            "product": self.product.id,
            "primary_mapping": True
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_primary_mapping_validation(self):

        url = "/api/vendor-product-mappings/"

        data = {
            "vendor": self.vendor.id,
            "product": self.product.id,
            "primary_mapping": True
        }

        self.client.post(url, data)

        product2 = Product.objects.create(
            name="Office",
            code="OFF",
            description="Office Suite"
        )

        data2 = {
            "vendor": self.vendor.id,
            "product": product2.id,
            "primary_mapping": True
        }

        response = self.client.post(url, data2)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)