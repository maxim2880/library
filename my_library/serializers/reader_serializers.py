from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from my_library.models import Reader, Book


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True)

    def validate(self, attrs):
        if len(attrs['books']) > 3:
            raise serializers.ValidationError('Не более 3 книг у читателя на руках')
        return attrs

    def update(self, instance, validated_data):
        if validated_data['books']:
            for book in validated_data['books']:
                if book not in instance.book.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise ValidationError(f'Книга {book.title} отсутствует')
            for book in instance.book.all():
                if book not in validated_data['books']:
                    book.quantity += 1
                    book.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Reader
        exclude = ['created_at', 'updated_at']
