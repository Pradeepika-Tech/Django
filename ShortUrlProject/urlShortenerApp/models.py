from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    long_url = models.URLField(unique=True)
    short_key = models.CharField(max_length=10, unique=True)  # You can adjust the length as needed

    def __str__(self):
        return f"{self.short_key}: {self.long_url}"