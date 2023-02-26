from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from my_library.models import Reader, Book


class ReaderSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True)

    def validate(self, attrs):
        if len(attrs['book']) > 3:
            raise serializers.ValidationError('Не более 3 книг у читателя на руках')
        return attrs

    def update(self, instance, validated_data):
        if validated_data['book']:
            for book in validated_data['book']:
                if book not in instance.book.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise ValidationError(f'The book {book.title} is missing')
            for book in instance.book.all():
                if book not in validated_data['book']:
                    book.quantity += 1
                    book.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Reader
        exclude = ['created_at', 'updated_at']
