from rest_framework.test import APITestCase
from rest_framework import status
from vendor.models import Vendor


class VendorAPITest(APITestCase):

    def test_create_vendor(self):

        url = "/api/vendors/"

        data = {
            "name": "Microsoft",
            "code": "MS",
            "description": "Cloud Vendor"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)

    def test_get_vendor_list(self):

        Vendor.objects.create(
            name="Google",
            code="GOOG",
            description="Cloud Vendor"
        )

        url = "/api/vendors/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)