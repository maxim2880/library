from django.contrib import admin
from my_library.models import Reader, Book, Author

admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Author)
