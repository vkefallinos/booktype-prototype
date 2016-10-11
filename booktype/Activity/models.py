from django.db import models


class Activity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    action = models.CharField(max_length=100,choices=(
        ('savechapter', 'saveChapter'),
        ('createchapter', 'createChapter'),
        ('deletechapter', 'deleteChapter'),
        ('createsection', 'createSection'),
        ('deletesection', 'deleteSection'),
        ('reordersection', 'reorderSection'),
        ('reorderchapter', 'reorderChapter'),
))
    revision = models.FloatField()


    def __str__(self):
        return "Activity"
