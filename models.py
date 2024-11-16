from django.db import models

# Create your models here.
# models.py
from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    category = models.CharField(max_length=100, choices=[
        ('popular', 'Popular'),
        ('trending', 'Trending'),
        ('tv_shows', 'TV Shows'),
        ('movies', 'Movies'),
        ('originals', 'Originals'),
    ])

    def __str__(self):
        return self.title
