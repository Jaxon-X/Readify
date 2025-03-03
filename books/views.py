
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .permissions import IsOwner
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwner]


    @action(detail=False, methods=['GET'], url_path="my-books")
    def my_books(self, request):
        books = Book.objects.filter(user_id=request.user)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)









