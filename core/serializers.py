from rest_framework import serializers
from smtplib import SMTPException
from django.core.mail import send_mail
from core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class EmailSerializer(serializers.Serializer):
    to_email = serializers.ListField(child=serializers.EmailField(max_length=256))
    subject = serializers.CharField()
    text = serializers.CharField()

    def save(self):
        """
        Send email using mailgun transactional API
        """
        to_email = self.validated_data.get("to_email")
        subject = self.validated_data.get("subject")
        text = self.validated_data.get("text")

        try:
            res = send_mail(
                subject,
                text,
                self.context["request"].user.email,
                to_email,
                fail_silently=False,
            )
            return res
        except SMTPException as e:
            print(f"There's an error: {e}")
            return None
