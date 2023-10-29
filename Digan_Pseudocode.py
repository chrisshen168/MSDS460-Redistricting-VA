import pulp
import pandas as pd

counties_df = pd.read_csv('VA_counties_red.csv')
counties_df.info()

counties_df['Geopoint'] = counties_df['Geopoint'].fillna('0, 0')
counties_df['Pop2023'] = counties_df['Pop2023'].fillna('0')

counties_df['Lat'] = counties_df['Geopoint'].astype(str).str.split(', ').str[0].astype("float")
counties_df['Long'] = counties_df['Geopoint'].astype(str).str.split(', ').str[1].astype("float")
counties_df['Pop2023'] = counties_df['Pop2023'].astype("int")

max_district = 11
max_district_size = 15
max_population = (counties_df['Pop2023'].sum() / 11) * 1.3
counties = counties_df['Name']

counties_df.head()

import math
from math import pi, pow, sin, cos, asin, sqrt, floor
from scipy import stats
import numpy as np
from pyproj import Proj

def degrees_to_radians(x):
     return((pi/180)*x)
     
def lon_lat_distance_miles(lon_a,lat_a,lon_b,lat_b):
    radius_of_earth = 24872/(2*pi)
    c = sin((degrees_to_radians(lat_a) - \
    degrees_to_radians(lat_b))/2)**2 + \
    cos(degrees_to_radians(lat_a)) * \
    cos(degrees_to_radians(lat_b)) * \
    sin((degrees_to_radians(lon_a) - \
    degrees_to_radians(lon_b))/2)**2
    return(2 * radius_of_earth * (asin(sqrt(c))))    
    
# Glendale, CA, latitude 34.142509, and longitude is -118.255074  
# Pasadena latitude and longitude coordinates are: 34.156113, -118.131943
print() 
print("Glendale to Pasadena distances computed directly from lon/lat:")
print("miles: ",lon_lat_distance_miles(-118.255074 ,34.142509,-118.131943,34.156113))

counties_Lat_Dic = dict(zip(counties_df.Name, counties_df.Lat))
counties_Long_Dic = dict(zip(counties_df.Name, counties_df.Long))
counties_Pop_Dic = dict(zip(counties_df.Name, counties_df.Pop2023))

def compactness(district):
    distance_list = []
    for og_county in district:
        for compare_county in district:
            distance = lon_lat_distance_miles(counties_Long_Dic[og_county], counties_Lat_Dic[og_county],
                                              counties_Long_Dic[compare_county], counties_Lat_Dic[compare_county])
            distance_list.append(distance)
    compact_score = sum(distance_list) / len(distance_list)
    return compact_score

def total_pop(district):
    population = 0
    for county in district:
        population += counties_Pop_Dic['county']
    return population

from itertools import chain, combinations
min_len = 2
max_len = 6
possible_districts = list(chain.from_iterable(combinations(counties, i) for i in range(min_len, max_len+1)))

#create a binary variable to state that a district is used
x = pulp.LpVariable.dicts('district', possible_districts, 
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

redistrict_model = pulp.LpProblem("Redistricting Model", pulp.LpMinimize)


redistrict_model += sum([compactness(district) * x[district] for district in possible_districts])
print(redistrict_model)

#specify the population max
for district in possible_districts:
    redistrict_model += total_pop(district) * x[district] <= max_population, f"Max_people_in_{district}"

#specify the maximum number of districts
redistrict_model += sum([x[district] for district in possible_districts]) == max_district, "Maximum_number_of_districts"

#A county can be assigned to one and only one district
for county in counties:
    redistrict_model += sum([x[district] for district in possible_districts if county in district]) == 1, "Must_zone_%s"%county
    
redistrict_model.solve()

print("The choosen districts are out of a total of %s:"%len(possible_districts))
for district in possible_districts:
    if x[district].value() == 1.0:
        print(district)
