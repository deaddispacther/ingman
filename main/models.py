from django.db import models


class Video(models.Model):
    txt = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.txt