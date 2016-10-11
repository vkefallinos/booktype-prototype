from django.db import models
from booktype.BookTypeUser.models import BookTypeUser
from booktype.SubComment.models import SubComment


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    selected_text = models.TextField()
    resolved = models.BooleanField()

    user = models.ForeignKey(BookTypeUser, related_name='user_comments')
    subcomments = models.ManyToManyField(SubComment, related_name='subcomments_comments')

    def __str__(self):
        return "Comment"
