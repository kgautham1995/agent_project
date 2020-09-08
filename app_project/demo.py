
from geopy.geocoders import Nominatim
# from app_project.models import agent_model


geolocator = Nominatim(user_agent="app")
location = geolocator.geocode("Hyderabad")
address1 = location.address
lat = location.latitude
long = location.longitude
print(address1,lat,long)
