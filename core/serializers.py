from rest_framework import serializers
from core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def update(self, instance, validated_data):
        print(validated_data, "data")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        print(instance.date_of_birth)
        instance.save()
        return instance
