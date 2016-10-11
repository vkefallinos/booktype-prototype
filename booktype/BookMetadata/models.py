from django.db import models


class BookMetadata(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100,)
    short_title = models.CharField(max_length=100,)
    subtitle = models.TextField()
    publisher = models.CharField(max_length=100,)
    publication_date = models.DateField()
    copyright_date = models.DateField()
    copyright_holder = models.CharField(max_length=100,)
    publisher_city = models.CharField(max_length=100,)
    short_description = models.CharField(max_length=100,)
    long_description = models.TextField()
    ebook_isbn = models.CharField(max_length=100,)
    print_isbn = models.CharField(max_length=100,)


    def __str__(self):
        return "BookMetadata"
