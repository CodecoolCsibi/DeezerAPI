from django.db import models


class Artist(models.Model):
    deezer_id = models.IntegerField()
    name = models.CharField(max_length=200)
    picture_URL = models.CharField(max_length=200)


class Genre(models.Model):
    deezer_id = models.IntegerField()
    name = models.CharField(max_length=200)
    picture_URL = models.CharField(max_length=200)


class Album(models.Model):
    deezer_id = models.IntegerField()
    title = models.CharField(max_length=300)
    cover_picture_URL = models.CharField(max_length=300)
    genres = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist)


class Track(models.Model):
    deezer_id = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    rank = models.IntegerField()
    album = models.ForeignKey(Album)

