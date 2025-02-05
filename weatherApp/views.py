import requests
import os
from dotenv import load_dotenv
from django.shortcuts import render
from .models import HistoricalWeather
from datetime import datetime

def get_weather(city):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def weather_view(request):
    if request.method == 'POST':
        city = request.POST['city']
        weather_data = get_weather(city)
        HistoricalWeather.objects.create(
            city=city,
            date=datetime.now(),
            temperature=weather_data['main']['temp'],
            description=weather_data['weather'][0]['description']
        )
        return render(request, 'weatherApp/home.html', {'weather': weather_data})
    return render(request, 'weatherApp/home.html')
