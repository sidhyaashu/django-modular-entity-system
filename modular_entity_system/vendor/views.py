from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreateAPIView(APIView):

    def get(self, request):

        vendors = Vendor.objects.all()

        serializer = VendorSerializer(vendors, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    

class VendorDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Vendor.objects.get(pk=pk)

        except Vendor.DoesNotExist:
            return None

    def get(self, request, pk):

        vendor = self.get_object(pk)

        if not vendor:
            return Response({"error": "Vendor not found"}, status=404)

        serializer = VendorSerializer(vendor)

        return Response(serializer.data)

    def put(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        vendor = self.get_object(pk)

        vendor.delete()

        return Response(status=204)