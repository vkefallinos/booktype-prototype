from django.db import models


class Cover(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100,)
    creator = models.CharField(max_length=100,)
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
    notes = models.TextField()
    image = models.ImageField()
    approved = models.BooleanField()


    def __str__(self):
        return "Cover"
