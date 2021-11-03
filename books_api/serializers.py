from rest_framework import serializers
from Books.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'description', 'author', 'isbn')
