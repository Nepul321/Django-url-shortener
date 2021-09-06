from django.db import models

class URL(models.Model):
    url = models.URLField()
    visits = models.IntegerField(default=0)
    url_id = models.CharField(max_length=255)

    def __str__(self):
        return self.url_id