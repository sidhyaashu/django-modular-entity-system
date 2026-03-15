from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = VendorProductMapping.objects.all()

        serializer = VendorProductMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return VendorProductMapping.objects.get(pk=pk)

        except VendorProductMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(mapping)

        return Response(serializer.data)

    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        mapping = self.get_object(pk)

        mapping.delete()

        return Response(status=204)