from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(req):
    # return HttpResponse('Hello World')
    
    # data = {
    #     'movies': [
    #         {
    #             'id': 1,
    #             'title': 'Meg',
    #             'year': 2019
    #         },
    #         {
    #             'id': 2,
    #             'title': 'Jaws',
    #             'year': 1969
    #         },
    #         {
    #             'id': 3,
    #             'title': 'Sharknado',
    #             'year': 1990
    #         },
    #     ]
    # }

    data = Movie.objects.all()

    return render(req, 'movies/movies.html', {'movies': data})

def home(req):
    return HttpResponse('Home Page')

def detail(req, id):
    data = Movie.objects.get(pk=id)
    return render(req, 'movies/detail.html', {'movie': data})

def add(req):
    title = req.POST.get('title')
    year = req.POST.get('year')
    
    # print(title, year)

    if year and title:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(req, 'movies/add.html') 


def delete(req, id):
    Movie.objects.get(pk=id).delete()
  
    return HttpResponseRedirect('/movies')
 