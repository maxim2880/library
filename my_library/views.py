from rest_framework import viewsets, filters

from my_library.models import Author, Book, Reader
from my_library.serializers.author_serializers import AuthorSerializer
from my_library.serializers.book_serializers import BookSerializer
from my_library.serializers.reader_serializers import ReaderSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['name', 'surname']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'surname', 'phone_number']

    def perform_destroy(self, instance: Reader):
        instance.is_active = False
        instance.save()
