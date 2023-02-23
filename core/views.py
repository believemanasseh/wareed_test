from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from core.models import Student
from core.serializers import StudentSerializer


class StudentView(APIView):
    """
    Retrieve and create student objects
    """

    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    @swagger_auto_schema(
        query_serializer=serializer_class,
        operation_description="Retrieve students",
        tags=["Core"],
    )
    def get(self, request, *args, **kwargs):
        param = request.query_params.get("name")
        if param:
            students = Student.objects.filter(name__icontains=param)
            if not students:
                return Response(
                    {
                        "status": "success",
                        "message": "No student found with such keyword",
                    },
                    status=status.HTTP_200_OK,
                )
        else:
            students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(
            {
                "status": "success",
                "message": "Student(s) retrieved successfully",
                "total_resources": students.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_description="Create student",
        tags=["Core"],
    )
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Student created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": "error",
                "message": "Invalid request",
                "error": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class StudentDetailView(APIView):
    """
    Retrieve, update and delete student object
    """

    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @swagger_auto_schema(
        query_serializer=serializer_class,
        operation_description="Retrieve student",
        tags=["Core"],
    )
    def get(self, request, id, *args, **kwargs):
        student = self.get_object(id)
        if not student:
            return Response(
                {"status": "error", "message": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = StudentSerializer(student)
        return Response(
            {
                "status": "success",
                "message": "Student object retrieved successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_description="Update student",
        tags=["Core"],
    )
    def put(self, request, id, *args, **kwargs):
        student = self.get_object(id)
        if not student:
            return Response(
                {"status": "error", "message": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Student object updated successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {
                "status": "error",
                "message": "Invalid request",
                "error": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        operation_description="Delete student",
        tags=["Core"],
    )
    def delete(self, request, id, *args, **kwargs):
        student = self.get_object(id)
        if not student:
            return Response(
                {"status": "error", "message": "Object not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        student.delete()
        return Response(
            {"status": "success", "message": "Student object deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
