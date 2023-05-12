import requests
from django.shortcuts import render
from .models import City
from .Forms import CityForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d164d18399c674cc6fe86615b1e32ed8'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(city_weather)  # add the data for the current city into our list
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)


