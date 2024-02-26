from rest_framework import serializers
from .models import Document

class DocxUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields='__all__'