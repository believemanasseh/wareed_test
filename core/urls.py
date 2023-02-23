from django.urls import path
from core.views import StudentView, StudentDetailView

urlpatterns = [
    path("students", StudentView.as_view(), name="student"),
    path("students/<int:id>", StudentDetailView.as_view(), name="student-detail"),
]
