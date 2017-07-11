from django.db import models

# Create your models here.
class Albums(models.Model):
    label = models.CharField(max_length=72)
    thumbnail_path = models.CharField(max_length=1000)

class Photo(models.Model):
    label = models.CharField(max_length=72)
    description = models.CharField(max_length=250)
    upload_time = models.DateTimeField()
    file_path = models.CharField(max_length=1000)
    belong_album_1 = models.BooleanField()
    belong_album_2 = models.BooleanField()
    belong_album_3 = models.BooleanField()
    belong_album_4 = models.BooleanField()
    belong_album_5 = models.BooleanField()
    belong_album_6 = models.BooleanField()
