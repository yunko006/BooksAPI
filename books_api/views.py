from rest_framework import generics
from Books.models import Books
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
