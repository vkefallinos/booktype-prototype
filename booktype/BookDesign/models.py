from django.db import models


class BookDesign(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    theme = models.CharField(max_length=100,choices=(
        ('academic', 'academic'),
        ('academiccomfortable', 'academiccomfortable'),
        ('artsyboldcomfortable', 'artsyboldcomfortable'),
        ('artsyboldcompact', 'artsyboldcompact'),
        ('bauhauscomfortable', 'bauhauscomfortable'),
        ('bauhauscompact', 'bauhauscompact'),
        ('commonsensecomfortable', 'commonsensecomfortable'),
        ('commonsensecompact', 'commonsensecompact'),
        ('custom', 'custom'),
        ('fairytalecomfortable', 'fairytalecomfortable'),
        ('fairytalecompact', 'fairytalecompact'),
        ('historicalfictioncomfortable', 'historicalfictioncomfortable'),
        ('historicalfictioncompact', 'historicalfictioncompact'),
        ('modernreportcomfortable', 'modernreportcomfortable'),
        ('modernreportcompact', 'modernreportcompact'),
        ('newfictioncomfortable', 'newfictioncomfortable'),
        ('newfictioncompact', 'newfictioncompact'),
        ('novelclassiccomfortable', 'novelclassiccomfortable'),
        ('novelclassiccompact', 'novelclassiccompact'),
        ('typewritercomfortable', 'typewritercomfortable'),
        ('typewritercompact', 'typewritercompact'),
))
    heading = models.CharField(max_length=100,)
    color = models.CharField(max_length=100,)
    font_size = models.IntegerField()
    alignment = models.CharField(max_length=100,)
    paragraph = models.TextField()
    text_indent = models.IntegerField()
    line_height = models.IntegerField()


    def __str__(self):
        return "BookDesign"
