from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name_plural='director'
    #movie=models.ManyToManyField(Movie)
    #id=models.AutoField(primary_key=True)
    director=models.CharField(max_length=50,default="None")
    #object_id = models.PositiveIntegerField(db_index=True, null=True, blank=True)
    def __str__(self):
        return str(self.director)


class Movie(models.Model):
    movie_name=models.CharField(max_length=200)
    description=models.TextField()
    #artist=models.CharField(max_length=100,default='None')
    director=models.ForeignKey(Director,null=True,blank=True)
    production_house=models.CharField(max_length=100,default='None')
    rating=models.DecimalField(default=1,max_digits=2,decimal_places=1)
    date=models.DateField(null=True)

    def __str__(self):
        return str(self.movie_name)

class Genre(models.Model):
    class Meta:
        verbose_name_plural='gener'
    movie=models.ManyToManyField(Movie)
    genre=models.CharField(max_length=10)
    def __str__(self):
        return str(self.genre)



class Artist(models.Model):
    class Meta:
        verbose_name_plural='Artists'
    movie=models.ManyToManyField(Movie)
    artist=models.CharField(max_length=50,default="None")
    def __str__(self):
        return str(self.artist)
