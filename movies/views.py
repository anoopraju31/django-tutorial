from django.http import HttpResponse
from django.shortcuts import render

def movies(req):
    # return HttpResponse('Hello World')
    
    data = {
        'movies': [
            {
                'id': 1,
                'title': 'Meg',
                'year': 2019
            },
            {
                'id': 2,
                'title': 'Jaws',
                'year': 1969
            },
            {
                'id': 3,
                'title': 'Sharknado',
                'year': 1990
            },
        ]
    }

    return render(req, 'movies/movies.html', data)

def home(req):
    return HttpResponse('Home Page')