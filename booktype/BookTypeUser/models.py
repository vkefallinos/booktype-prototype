from django.db import models


class BookTypeUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    email = models.EmailField()
    fullName = models.CharField(max_length=100,)
    about = models.TextField()
    profile_image = models.ImageField()
    public_email = models.EmailField()
    twitter = models.CharField(max_length=100,)
    facebook = models.CharField(max_length=100,)
    linked_in = models.CharField(max_length=100,)
    youtube = models.CharField(max_length=100,)
    vimeo = models.CharField(max_length=100,)
    hashed_password = models.CharField(max_length=100,)
    preferred_Language = models.CharField(max_length=100,)


    def __str__(self):
        return "BookTypeUser"
