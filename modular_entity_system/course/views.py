from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modular_entity_system.utils import get_object_or_404
from .models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):

    def get(self, request):

        product_id = request.GET.get("product_id")

        courses = Course.objects.all().order_by("-created_at")

        if product_id:
            courses = courses.filter(
                productcoursemapping__product_id=product_id
            )

        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CourseDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(Course, pk)

    def get(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course)

        return Response(serializer.data)

    def put(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        course = self.get_object(pk)

        course.delete()

        return Response(status=204)