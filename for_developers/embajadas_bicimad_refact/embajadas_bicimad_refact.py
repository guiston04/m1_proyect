

#import libraries

import pandas as pd
from shapely.geometry import Point
import geopandas as gpd


#Creamos las listas que nos van a permitir crear nuestro dataframe final
#Para Bicimad

def listas_bicimad_longitudes(df_bicimad):
    bicimad_longitudes = df_bicimad['longitude'].tolist()
    return bicimad_longitudes

def listas_bicimad_station_names(df_bicimad):
    bicimad_station_name = df_bicimad['name'].tolist()
    return bicimad_station_name

def listas_bicimad_addresses(df_bicimad):
    bicimad_station_address = df_bicimad['address'].tolist()
    return bicimad_station_address

def listas_bicimad_latitudes(df_bicimad):
    bicimad_latitudes = df_bicimad['latitude'].tolist()
    return bicimad_latitudes

#Para embajadas y consulados

def embajadas_latitudes(df_consulados_embajadas):
    consulados_embajadas_latitudes = df_consulados_embajadas['latitude'].tolist()
    return consulados_embajadas_latitudes

def embajadas_longitudes(df_consulados_embajadas):
    consulados_embajadas_longitudes = df_consulados_embajadas['longitud'].tolist()
    return consulados_embajadas_longitudes

def embajadas_titles(df_consulados_embajadas):
    place_of_interest = df_consulados_embajadas['title'].tolist()
    return place_of_interest

def embajadas_type(type_of_place, place_of_interest):
    type_of_place = [type_of_place for p in range (len(place_of_interest)-1)]
    return type_of_place

def embajadas_address(df_consulados_embajadas):
    place_address = df_consulados_embajadas['address.street-address'].tolist()
    return place_address

#Funciones para calcular distancias emabaja vs bicimad station
def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)

#función de creación de listas con resultado bicimad más próximo por cada embajada consulado

def creacion(consulados_embajadas_latitudes, consulados_embajadas_longitudes, bicimad_latitudes, bicimad_longitudes, df_bicimad, distances_final, addresses_bicimad_stations_final, bicimad_stations_final):
    for i in range(len(consulados_embajadas_latitudes)):
        print(f'{round(i/len(consulados_embajadas_latitudes)*100,1)}%')
        lati_start = consulados_embajadas_latitudes[i]
        longi_start = consulados_embajadas_longitudes[i]
        distances = []
        distances_sorted = []
        for n in range(len(bicimad_latitudes)-1):
            lat_finish = float(bicimad_latitudes[n])
            long_finish = float(bicimad_longitudes[n])
            distance = distance_meters(lati_start, longi_start, lat_finish, long_finish)
            distance = str(distance).split(" ")
            distance = distance[4]
            distance = distance.split("\nd")
            distance = float(distance[0])
            distances.append(distance)
            distances_sorted.append(distance)
    
        distances_sorted.sort()
        index = distances.index(distances_sorted[0])
        cond = (df_bicimad['latitude'] == bicimad_latitudes[index])
        address_bicimad_station = df_bicimad[cond].address.values[0]
        bicimad_station = df_bicimad[cond].name.values[0]
        distance_min = distances_sorted[0]
        distances_final.append(distance_min)
        addresses_bicimad_stations_final.append(address_bicimad_station)
        bicimad_stations_final.append(bicimad_station)
    return distances_final, addresses_bicimad_stations_final, bicimad_stations_final


#Juntamos las columnas en un mismo dataframe para tener
def dataframe(place_of_interest, type_of_place, place_address, bicimad_stations_final, addresses_bicimad_stations_final): 
    dataframe_result = pd.DataFrame(list(zip(place_of_interest, type_of_place, place_address, bicimad_stations_final,addresses_bicimad_stations_final)),
                columns =['Place of interest', 'type of place', 'place address', 'Bicimad station', 'Station Location'])
    return dataframe_result


#guardamos este dataframe para acceder a él cuando ya se haga query

def save(df, path_save_file):
    df.to_csv(path_save_file)
    return "saved correctly"
