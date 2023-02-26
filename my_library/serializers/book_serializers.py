from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from my_library.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='surname', many=True)

    class Meta:
        model = Book
        exclude = ['created_at', 'updated_at']
        validators = [UniqueTogetherValidator(queryset=Book.objects.all(), fields=['name', 'author'])]
