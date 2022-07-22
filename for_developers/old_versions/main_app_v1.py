

#import libraries

import pandas as pd
from bicimad_refact import bicimad_refact as br
from embajadas_refact import embajadas_refact as er 
from embajadas_bicimad_refact import embajadas_bicimad_refact as ebr
import os
from dotenv import load_dotenv

#BICIMAD STATIONS
#PARAMETERS
#connection string in order to connect to database de BiciMad


#EMBAJADAS
#PARAMETERS

path_embajadas = 'https://datos.madrid.es/egob/catalogo/201000-0-embajadas-consulados.json'
nombre_columna = 'location.latitude'
nuevo_nombre_columna = 'latitude'
nombre_columna_2 = 'location.longitude'
nuevo_nombre_columna_2 = 'longitud'
path_directory_embajadas = './files/df_consulados_embajadas.csv'


#EMBAJADAS VS BICIMAD
#PARAMETERS

#df_consulados_embajadas = pd.read_csv('/Users/guillaumedieude/Desktop/Ironhack/proyecto_m1/m1_proyect/for_developers/CSVs/df_consulados_embajadas.csv')
#df_bicimad = pd.read_csv('/Users/guillaumedieude/Desktop/Ironhack/proyecto_m1/m1_proyect/for_developers/CSVs/df_bicimad.csv')

type_of_place = "embajada/consulado"

distances = []
distances_sorted=[]
distances_index = []
bicimad_stations = []
address_bicimad_stations = []
distances_final = []
bicimad_stations_final = []
addresses_bicimad_stations_final = []


path_save_file = './files/df_embajadas_bicimad.csv'



if __name__ == "__main__":
    print("pipeline started")
    load_dotenv('token.env')
    token = os.environ.get("token")
    #APLICACION FUNCIONES BICIMAD_REFACT
    #creation del objeto engine para acceder a datos de BiciMad
    connection_string = 'mysql+pymysql://ironhack_user:' + token + '@173.201.189.217/BiciMAD'
    engine = br.engine(connection_string)
    print("engine created")
    #guardamos en un df los datos de Bicimad
    df_bicimad = pd.read_sql_query("SELECT * FROM bicimad_stations", engine)
    print("df_bicimad created")
    #Creación dataframe y aplicación de las funciones de transformación al dataframe df_bicimad
    df_bicimad['longitude'] = df_bicimad.apply(lambda x: br.latitudes(x['geometry.coordinates']), axis=1 )
    df_bicimad['latitude'] = df_bicimad.apply(lambda x: br.longitudes(x['geometry.coordinates']), axis=1 )
    print("df_bicimad modified")
    #Reducción del dataframe para quedarnos solo con lo que nos interesa
    df_bicimad = df_bicimad[['name', 'address', 'latitude','longitude']]
    print("df_bicimad reduced")
    #Descarga del dataframe a csv
    df_bicimad.to_csv("./files/df_bicimad.csv")
    print("df_bicimad saved")
    #APLICACION FUNCIONES EMBAJADAS_REFACT
    df_consulados_embajadas = er.df_embajadas(path_embajadas)
    print("df_consulados_embajadas created")
    #Renombramos columnas que representan la latitud y la longitud
    df_consulados_embajadas = er.clean_df_embajadas(df_consulados_embajadas, nombre_columna,nuevo_nombre_columna,nombre_columna_2, nuevo_nombre_columna_2)
    print("df_consulados_embajadas cleaned")
    #Reducimos el dataframe a las columnas que nos interesan
    df_consulados_embajadas = er.df_embajadas_reducido(df_consulados_embajadas)
    print("df_consulados_embajadas reduced")
    #Quitamos líneas que tienen como valor nulo la latitud o longitud
    df_consulados_embajadas = er.dropna_embajadas(df_consulados_embajadas)
    print("df_consulados_embajadas sin na")
    #Descarga del dataframe a csv
    df_consulados_embajadas_saved = er.descargar_embajadas(df_consulados_embajadas, path_directory_embajadas)
    print("df_consulados_embajadas saved")
    #APLICACION FUNCIONES EMBAJADAS_BICIMAD_REFACT
    #Creamos las listas que nos van a permitir crear nuestro dataframe final
    #Para Bicimad
    bicimad_longitudes = ebr.listas_bicimad_longitudes(df_bicimad)
    bicimad_station_name = ebr.listas_bicimad_station_names(df_bicimad)
    bicimad_station_address = ebr.listas_bicimad_addresses(df_bicimad)
    bicimad_latitudes = ebr.listas_bicimad_latitudes(df_bicimad)
    print("lists bicimad created")
    #Para embajadas y consulados
    consulados_embajadas_latitudes = ebr.embajadas_latitudes(df_consulados_embajadas)
    consulados_embajadas_longitudes = ebr.embajadas_longitudes(df_consulados_embajadas)
    place_of_interest = ebr.embajadas_titles(df_consulados_embajadas)
    type_of_place = ebr.embajadas_type(type_of_place, place_of_interest)
    place_address = ebr.embajadas_address(df_consulados_embajadas)
    print("lists embassy created")
    #función de creación de listas con resultado bicimad más próximo por cada embajada consulado
    print("creación empezada")
    a, b, c = ebr.creacion(consulados_embajadas_latitudes, consulados_embajadas_longitudes,bicimad_latitudes, bicimad_longitudes, df_bicimad, distances_final, addresses_bicimad_stations_final, bicimad_stations_final)
    distances_final = a
    addresses_bicimad_stations_final = b
    bicimad_stations_final = c
    #Juntamos las columnas en un mismo dataframe para tener
    dataframe_result = ebr.dataframe(place_of_interest, type_of_place, place_address, bicimad_stations_final, addresses_bicimad_stations_final)
    print(dataframe_result)
    print("dataframe correctamente creado")
    #Descarga del dataframe a csv
    save_dataframe = ebr.save(dataframe_result, path_save_file)
    print("result saved")