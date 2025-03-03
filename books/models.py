from django.db import models

from users.models import CustomUserModel

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="books")
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="book_files/")
    cover_image = models.ImageField(upload_to="book_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




