from django.db import models
from booktype.Chapter.models import Chapter


class Section(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100,)

    chapters = models.ManyToManyField(Chapter, related_name='chapters_sections')

    def __str__(self):
        return "Section"
