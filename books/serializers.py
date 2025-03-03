
from rest_framework import serializers
from .models import Book, Category
from django.conf import settings

class BookSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    cover_image_url = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Book
        fields = ["id", "title",  "description","file", "cover_image", "file_url", "cover_image_url", "uploaded_at", "user_id", "category_id"]

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super().create(validated_data)

    def get_file_url(self, obj):
        return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{obj.file.name}"

    def get_cover_image_url(self, obj):
        return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{obj.cover_image.name}"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


