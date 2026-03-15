from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):

    def get(self, request):

        product_id = request.GET.get("product_id")

        courses = Course.objects.all()

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

        try:
            return Course.objects.get(pk=pk)

        except Course.DoesNotExist:
            return None

    def get(self, request, pk):

        course = self.get_object(pk)

        if not course:
            return Response({"error": "Course not found"}, status=404)

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