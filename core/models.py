from django_extensions.db.models import TimeStampedModel
from django.core.validators import validate_email
from django.db import models


class Student(TimeStampedModel):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, unique=True, validators=[validate_email])
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.name
