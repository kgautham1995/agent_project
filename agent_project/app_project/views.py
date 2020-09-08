from django.shortcuts import render
from geopy.geocoders import Nominatim
from app_project.models import agent_model
from app_project import middleware

# Create your views here.
def home(request):

    return render(request, "index.html")



def locate(request):
    dict_data=agent_model.objects.all()
    lat=0
    long=0
    address1=""
    for x in dict_data:
        geolocator = Nominatim(user_agent="app")
        location = geolocator.geocode(x.city)
        address1 = location.address
        lat = location.latitude
        long = location.longitude
        print(address1, lat, long)

    return render(request)