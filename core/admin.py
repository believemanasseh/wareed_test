from django.contrib import admin
from core import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "number",
        "name",
        "faculty_name",
        "email",
        "date_of_birth",
        "created",
        "modified",
    ]
    list_filter = ["id", "number", "faculty_name"]
    search_fields = ["email", "name", "number", "faculty_name"]


admin.site.site_title = "Student API"
admin.site.site_header = "Student API"
