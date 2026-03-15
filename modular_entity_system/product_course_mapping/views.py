from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = ProductCourseMapping.objects.all()

        serializer = ProductCourseMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return ProductCourseMapping.objects.get(pk=pk)

        except ProductCourseMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(mapping)

        return Response(serializer.data)

    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        mapping = self.get_object(pk)

        mapping.delete()

        return Response(status=204)