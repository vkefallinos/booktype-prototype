from django.db import models
from booktype.BookTypeUser.models import BookTypeUser
from booktype.BookTypeUser.models import BookTypeUser
from booktype.Book.models import Book


class BookTypeGroup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100,)
    description = models.TextField()
    image = models.ImageField()

    owner = models.ForeignKey(BookTypeUser, related_name='owner_booktypegroups')
    members = models.ManyToManyField(BookTypeUser, related_name='members_booktypegroups')
    books = models.ManyToManyField(Book, related_name='books_booktypegroups')

    def __str__(self):
        return "BookTypeGroup"
