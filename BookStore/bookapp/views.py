from rest_framework import viewsets
from .Serializer import BookSerilizer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer