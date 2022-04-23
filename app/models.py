from django.db import models
# Create your models here.

class Url(models.Model):
    url = models.URLField('Url', max_length=255)
    short_url = models.URLField('Url-short', max_length=255)

    def __str__(self):
        return self.url

