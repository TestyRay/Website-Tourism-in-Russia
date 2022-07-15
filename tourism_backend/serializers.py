from rest_framework import serializers
from .models import Application


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            "id", "name", "mobile_phone",
            "email", "comment", "date",
        )