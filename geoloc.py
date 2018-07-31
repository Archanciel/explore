import math, json, collections, itertools
import numpy as np
import matplotlib.pyplot as pp
#%matplotlib inline
from mpl_toolkits.basemap import Basemap
import geopy

cities, years = [], []

for game in open('games.txt', 'r'):
    words = game.split()

    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)

    geolocator = geopy.geocoders.Nominatim()

    locations = {}

for city in cities:
    print("Locating", city)
    locations[city] = geolocator.geocode(city.split('/')[0])

pp.figure(figsize=(10,5))

world = Basemap()
world.drawcoastlines(linewidth=0.25)
world.drawcountries(linewidth=0.25)

for city,pos in locations.items():
    world.plot(pos.longitude,pos.latitude,'r.',markersize=10,latlon=True)

if __name__ == '__main__':
    pass