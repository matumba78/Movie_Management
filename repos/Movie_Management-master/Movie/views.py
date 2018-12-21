from django.shortcuts import render
from django.views.generic import View
from .models import Genre,Movie,Director,Artist
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db import connection

class Newmovie(View):
    def post(self,request):
      try:
        movie_name=request.POST["movie_name"]
        description=request.POST["description"]
        #director=request.POST["director"]
        production_house=request.POST["production_house"]
        genre=request.POST["genre"]
        director=request.POST["director"]
        artist=request.POST["artist"]
        date=request.POST["date"]
        rating=request.POST["rating"]
        dir=Director(director=director)
        dir.save()
        data=Movie(movie_name=movie_name,description=description,director=dir,production_house=production_house,date=date,rating=rating)
        data.save()
        dat=Genre(genre=genre)
        art=Artist(artist=artist)
        dat.save()
        #dir.save()
        art.save()
        #dir.movie.add(data)
        art.movie.add(data)
        dat.movie.add(data)
        return HttpResponse("Movie Added Successfully",status=201)
      except Exception as e:
          return HttpResponse("Internal Server Error", status=500)



class Searchbygenre(View):
    def get(self,request,genre):
        obj=Genre.objects.filter(genre=genre)
        if obj:
            res=[]
            for genre in obj:
                for movie in genre.movie.all():
                    res.append ({
                    'movie_name' : movie.movie_name,
                    'description' : movie.description,
                    'production_house' : movie.production_house,
                    'rating': str(movie.rating),
                                      })
                    #res.append(gemovie)
                    #res.append("<br>")

        #return HttpResponse("Action Movies :" + str(res))


            return HttpResponse(json.dumps(res),content_type='application/json',status=200)
        else:
            return HttpResponse(json.dumps("Invalid Genre"),status=400)


class Searchbydirector(View):
    def get(self,request,director):
        obj=Movie.objects.filter(director__director=director)
        if obj:
            res=[]
            for i in obj:
                res.append ({
                'movie_name' : i.movie_name,
                'description' : i.description,
                'production_house' : i.production_house,
                'rating': str(i.rating),
                                  })
                    #res.append(movie)
                    #res.append("<br>")
            print len(connection.queries)
            return HttpResponse(json.dumps(res),content_type='application/json',status=200)
        else:
            return HttpResponse(json.dumps("No movies found with director named " + str(director)),status=400)


class MonthlyRelease(View):
    def get(self,request,year,month,day):
        obj=Movie.objects.filter(date__year=year,date__month=month)
        if obj:
            res=[]
            for movie in obj:
                res.append ({
                'movie_name' : movie.movie_name,
                'description' : movie.description,
                'production_house' : movie.production_house,
                'rating':str(movie.rating),

                                  })
                #res.append(movie)
                #res.append("<br>")
            return HttpResponse(json.dumps(res),content_type='Application/Json',status=200)
        else:
            return HttpResponse(json.dumps("No Movie Found on the given Release date"))


class Search(View):
    def get(self,request,movie):
        #minimum three characters needed
        obj=Movie.objects.filter(movie_name__istartswith=movie)
        if obj:
            res=[]
            for i in obj:
                res.append ({
                'movie_name' : i.movie_name,
                                  })
            return HttpResponse(json.dumps(res),content_type='Application/json',status=200)
        else:
            return HttpResponse(json.dumps("No Movie found "))

class Actorstats(View):

    def get(self,request,artist):
        from django.db import connection

        obj=Artist.objects.filter(artist=artist).prefetch_related('movie')
        #print len(connection.queries)
        if obj:
              res=[]
              #res.append("<b>Actor Stats</b>")
              #res.append("<br>")
              #res.append("<b>Movie List</b>")
              #res.append("<br>")
              for artist in obj:
                  for movie in artist.movie.all():
                      res.append({
                      'movie_name':movie.movie_name
                      })
                    #  res.append(movie)
                     # res.append("<br>")
              #print len(connection.queries)


              #res.append("<b>Average Rating </b>")
              a=0
              count=0
              for artist in obj:
                  for movie in artist.movie.all():
                      a=a+movie.rating
                      count+=1
                  average=round(a/count,1)
              res.append({
              'Average Rating':str(average)
              })
              max=0
              for artist in obj:
                  for movie in artist.movie.all():
                      if max < movie.rating:
                          max=movie.rating
                          a=movie
                  #res.append("<b>Top Rated Movie</b>")
                  #res.append("<br>")
                  #res.append(a)
              res.append({
              'Top Rated Movie':str(a)
              })
              #print len(connection.queries)
              #print json.dumps(connection.queries)
              return HttpResponse(json.dumps(res),content_type='Application/json')
        else:
            return HttpResponse("No records found ")
