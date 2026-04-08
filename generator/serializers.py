from rest_framework import serializers
from .models import Template, GeneratedDocument


class TemplateSerializer(serializers.ModelSerializer):
    preview_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Template
        fields = ['id', 'title', 'category', 'description', 'html_layout',
                  'css_layout', 'preview_image_url', 'sample_data', 'fields_schema']

    def get_preview_image_url(self, obj):
        if obj.preview_image:
            return obj.preview_image.url
        return None


class GeneratedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedDocument
        fields = ['id', 'template', 'title', 'data', 'rendered_html', 'created_at', 'updated_at']
        read_only_fields = ['rendered_html', 'created_at', 'updated_at']
