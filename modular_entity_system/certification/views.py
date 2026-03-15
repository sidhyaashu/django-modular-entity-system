from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreateAPIView(APIView):

    def get(self, request):

        course_id = request.GET.get("course_id")

        certifications = Certification.objects.all()

        if course_id:
            certifications = certifications.filter(
                coursecertificationmapping__course_id=course_id
            )

        serializer = CertificationSerializer(certifications, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CertificationDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Certification.objects.get(pk=pk)

        except Certification.DoesNotExist:
            return None

    def get(self, request, pk):

        certification = self.get_object(pk)

        if not certification:
            return Response({"error": "Certification not found"}, status=404)

        serializer = CertificationSerializer(certification)

        return Response(serializer.data)

    def put(self, request, pk):

        certification = self.get_object(pk)

        serializer = CertificationSerializer(certification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        certification = self.get_object(pk)

        serializer = CertificationSerializer(certification, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        certification = self.get_object(pk)

        certification.delete()

        return Response(status=204)