# Generated by Django 4.1.7 on 2023-02-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_student_faculty_name_alter_student_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(),
        ),
    ]
