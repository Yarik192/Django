from django.db import models

"""CREATING A BOOK LIBRARY"""


class Reader(models.Model):
    full_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.full_name}"


class Author(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    name_of_book = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    co_author = models.ManyToManyField(Author, related_name="Соавтор", blank=True, verbose_name="Соавторы")

    reader = models.ForeignKey("Reader", on_delete=models.PROTECT, null=True, blank=True)
    taken = models.BooleanField("В наличии", default=True)

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name_of_book
