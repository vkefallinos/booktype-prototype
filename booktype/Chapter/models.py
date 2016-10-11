from django.db import models
from booktype.Comment.models import Comment


class Chapter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100,)
    content = models.TextField()
    status = models.CharField(max_length=100,)

    comments = models.ManyToManyField(Comment, related_name='comments_chapters')

    def __str__(self):
        return "Chapter"
