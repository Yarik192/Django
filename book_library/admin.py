from django.contrib import admin
from book_library.models import Author, Book, Reader


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name_of_book", "author"]


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
