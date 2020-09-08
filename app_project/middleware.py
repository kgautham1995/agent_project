import requests
from geopy.geocoders import Nominatim
import json
from app_project.models import agent_model

class geocodeMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Constructor")
        geo_code()

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("I am Call")
        return response


def geo_code():
    #response = requests.get("https://imdb8.p.rapidapi.com/title/auto-complete")
    dict_data=agent_model.objects.all()
    for x in dict_data:
        geolocator = Nominatim(user_agent="app")
        location = geolocator.geocode(x.city)
        print((location.latitude, location.longitude))
        print(location.raw)
    dict_data1 = json.loads(dict_data.text)
    json.dump(dict_data1, open("app_project/raw/agentdata.json", "w"))
    print("Data Written to File")