from django.db import models
from booktype.BookTypeUser.models import BookTypeUser


class SubComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    text = models.CharField(max_length=200,)

    user = models.ForeignKey(BookTypeUser, related_name='user_subcomments')

    def __str__(self):
        return "SubComment"
