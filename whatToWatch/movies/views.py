import os
import random
import requests
from django.conf import settings
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()

def random_movie(request):
    api_key = os.getenv('API_KEY')
    
    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json',
    }
    
    url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_250_BEST_FILMS&page=1'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        films = data.get('films', [])
        if films:
            movie = random.choice(films)
        else:
            movie = None
            
    except Exception as e:
        movie = None
        print(f"Ошибка при запросе к API: {e}")

    context = {
        'movie': movie,
    }

    return render(request, 'movies/random_movie.html', context)
