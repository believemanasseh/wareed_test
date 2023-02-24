from django.urls import path
from core.views import SendEmails, StudentView, StudentsByAge, StudentDetailView

urlpatterns = [
    path("students", StudentView.as_view(), name="student"),
    path("students/<int:id>", StudentDetailView.as_view(), name="student-detail"),
    path("students/search", StudentsByAge.as_view(), name="students-by-age"),
    path("students/send-email", SendEmails.as_view(), name="send-emails"),
]
