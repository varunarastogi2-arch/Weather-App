import requests
from django.shortcuts import render

API_KEY = '839da67ace3b9f7ec59247b517ba0021'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def index(request):
    city = request.GET.get('city') or request.POST.get('city')
    weather = None
    error = None

    if city:
        response = requests.get(
            API_URL,
            params={'q': city, 'appid': API_KEY, 'units': 'metric'},
            timeout=10,
        )
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temperature': round(data['main']['temp']),
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'feels_like': round(data['main']['feels_like']),
                'wind_speed': data['wind']['speed'],
            }
        else:
            error = 'City not found. Please try again.'

    return render(request, 'index.html', {
        'weather': weather,
        'error': error,
        'city': city or '',
    })
