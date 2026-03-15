from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modular_entity_system.utils import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(APIView):

    def get(self, request):

        vendor_id = request.GET.get("vendor_id")

        products = Product.objects.all().order_by("-created_at")

        if vendor_id:
            products = products.filter(
                vendorproductmapping__vendor_id=vendor_id
            )

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ProductDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(Product, pk)

    def get(self, request, pk):

        product = self.get_object(pk)

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def put(self, request, pk):

        product = self.get_object(pk)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        product = self.get_object(pk)

        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        product = self.get_object(pk)

        product.delete()

        return Response(status=204)