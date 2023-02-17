from django.db import models


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")


class Author(DatesModelMixin):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['created_at']

    name = models.CharField(verbose_name='Имя', max_length=40)
    surname = models.CharField(verbose_name='Фамилия', max_length=40)
    photo = models.ImageField(upload_to='authors/', blank=True, verbose_name="Фото автора")

    def __str__(self):

        return f"Author: {self.name}"


class Book(DatesModelMixin):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['created_at']

    name = models.CharField(verbose_name='Имя', max_length=40)
    description = models.CharField(verbose_name='Имя', max_length=1000)
    num_pages = models.PositiveSmallIntegerField(verbose_name="Количество страниц")
    author = models.ManyToManyField(Author)
    num_books = models.PositiveSmallIntegerField(verbose_name="Количество книг в библиотеке")

    def __str__(self):

        return f"Book: {self.name}"


class Reader(DatesModelMixin):
    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        ordering = ['created_at']

    name = models.CharField(verbose_name='Имя', max_length=40)
    surname = models.CharField(verbose_name='Фамилия', max_length=40)
    phone_number = models.PositiveBigIntegerField(verbose_name="Номер телефона")
    status = models.BooleanField(default=True, verbose_name="Статус читателя")
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):

        return f"Reader: {self.name}"
