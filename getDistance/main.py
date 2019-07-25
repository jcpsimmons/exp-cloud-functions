from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def calcDistanceInMiles(location1, location2):
    location1 = geolocator.geocode(location1)
    location1 = (location1.latitude, location1.longitude)
    location2 = geolocator.geocode(location2)
    location2 = (location2.latitude, location2.longitude)
    distanceInMiles = geodesic(location1, location2).miles
