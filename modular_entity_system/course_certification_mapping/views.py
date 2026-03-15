from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = CourseCertificationMapping.objects.all()

        serializer = CourseCertificationMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)

        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(mapping)

        return Response(serializer.data)

    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        mapping = self.get_object(pk)

        mapping.delete()

        return Response(status=204)