import urllib.request
import json
from django.shortcuts import render
from django.http import JsonResponse

def get_weather_info(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_url = 'http://api.openweathermap.org/data/2.5/weather?id=' + city + '&appid=b2f034c121b0599bb3cc1082cf7379cf'
        source = urllib.request.urlopen(api_url).read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        data['forcast']=False;
        return JsonResponse(data)
    else:
        data = {}

    return render(request ,'weather/index.html',data)



def get_weather_info_coordinate(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        api_url = 'http://api.openweathermap.org/data/2.5/weather?lat='+latitude +'&lon='+longitude+'&appid=b2f034c121b0599bb3cc1082cf7379cf'
        source = urllib.request.urlopen(api_url).read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        data['forcast']=False;
        return JsonResponse(data)
    else:
        data = {}
    return render(request ,'weather/index.html',data)



def get_weather_forcast(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_url = 'http://api.openweathermap.org/data/2.5/forecast?id='+ city +'&appid=b2f034c121b0599bb3cc1082cf7379cf'
        source = urllib.request.urlopen(api_url).read()
        list_of_data = json.loads(source)
        list_of_data['forcast']=True;
        # data = {
        # "country_code": str(list_of_data['sys']['country']),
        # "coordinate": str(list_of_data['coord']['lon']) + ', '
        # + str(list_of_data['coord']['lat']),

        # "temp": str(list_of_data['main']['temp']) + ' °C',
        # "pressure": str(list_of_data['main']['pressure']),
        # "humidity": str(list_of_data['main']['humidity']),
        # 'main': str(list_of_data['weather'][0]['main']),
        # 'description': str(list_of_data['weather'][0]['description']),
        # 'icon': list_of_data['weather'][0]['icon'],
        # }
        return JsonResponse(list_of_data)