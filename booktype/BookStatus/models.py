from django.db import models


class BookStatus(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    status = models.CharField(max_length=100,)


    def __str__(self):
        return "BookStatus"
