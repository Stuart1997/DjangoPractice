from django.db import models
from django.urls import reverse


# Each album created will give it an ID
class Album(models.Model):  # Every model inherits from this
    artist = models.CharField(max_length=100)   # Declare what the type of this field is
    albumTitle = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    albumImage = models.FileField()

    #Whenever an album is added, it'll give it a pk, and go to detail view
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


    def __str__(self):  # String representation of the object
        return self.albumTitle + " by " + self.artist


class Song(models.Model):
    # Foreign key - each song linked to an album, album PK = 1, so FK = 1
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Whenever album is deleted, songs also deleted
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):  # String representation of the object
        return self.songTitle