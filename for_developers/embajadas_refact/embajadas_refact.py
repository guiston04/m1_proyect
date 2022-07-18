

#Import libraries

import pandas as pd
import requests


def df_embajadas(path):
    #request a la api del ayuntamiento
    response = requests.get(path)
    #convertimos resultado request a un json
    json_data = response.json()
    #normalizamos/aplanamos todos los datos. En este caso solo nos interesa los datos dentro de la llave graph del diccionario.
    df_consulados_embajadas = pd.json_normalize(json_data["@graph"])
    #Convertimos a dataframe el json normalizado
    df_consulados_embajadas = pd.DataFrame(df_consulados_embajadas)
    return df_consulados_embajadas

#Renombramos columnas que representan la latitud y la longitud
def clean_df_embajadas(df, nombre_columna, nuevo_nombre_columna,nombre_columna_2, nuevo_nombre_columna_2):
    df_consulados_embajadas = df.rename({nombre_columna: nuevo_nombre_columna}, axis=1)
    df_consulados_embajadas = df_consulados_embajadas.rename({nombre_columna_2: nuevo_nombre_columna_2}, axis=1)
    return df_consulados_embajadas

#Reducimos el dataframe a las columnas que nos interesan

def df_embajadas_reducido(df):
    df_consulados_embajadas = df[['title', 'address.street-address', 'latitude','longitud']]
    return df_consulados_embajadas

#Quitamos líneas que tienen como valor nulo la latitud o longitud

def dropna_embajadas(df):
    df_consulados_embajadas = df.dropna()
    return df_consulados_embajadas

#Descarga del dataframe a csv

def descargar_embajadas(df, path_directory):
    df.to_csv(path_directory)
