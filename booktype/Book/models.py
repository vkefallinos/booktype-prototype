from django.db import models
from booktype.BookTypeUser.models import BookTypeUser
from booktype.BookMetadata.models import BookMetadata
from booktype.Role.models import Role
from booktype.Chapter.models import Chapter
from booktype.Section.models import Section
from booktype.Cover.models import Cover
from booktype.BookDesign.models import BookDesign


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100,)
    description = models.TextField()
    licence = models.CharField(max_length=100,choices=(
        ('arr', 'ARR'),
        ('ccby', 'CC BY'),
        ('ccby-nd', 'CC BY-ND'),
        ('ccby-nc', 'CC BY-NC'),
        ('ccby-nc-nd', 'CC BY-NC-ND'),
        ('ccby-nc-sa', 'CC BY-NC-SA'),
        ('ccby-sa', 'CC BY-SA'),
        ('cc0', 'CC0'),
        ('agpl', 'AGPL'),
        ('gpl', 'GPL'),
        ('mit', 'MIT'),
        ('pd', 'PD'),
))
    language = models.CharField(max_length=100,)
    right_to_left = models.BooleanField()
    public = models.BooleanField()
    image = models.ImageField()
    status = models.CharField(max_length=100,)
    created = models.DateTimeField()
    published = models.DateField()

    owner = models.ForeignKey(BookTypeUser, related_name='owner_books')
    metadata = models.ForeignKey(BookMetadata, related_name='metadata_books')
    roles = models.ManyToManyField(Role, related_name='roles_books')
    chapters = models.ManyToManyField(Chapter, related_name='chapters_books')
    sections = models.ManyToManyField(Section, related_name='sections_books')
    covers = models.ManyToManyField(Cover, related_name='covers_books')
    design = models.ForeignKey(BookDesign, related_name='design_books')

    def __str__(self):
        return "Book"
