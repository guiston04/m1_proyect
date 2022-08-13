import requests
from dotenv import load_dotenv
import os
import pandas as pd

#PARAMETERS

path_api = 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
email = 'gdieude@me.com'
password = 'CBzt6n.n3RmRewn'
env_file = 'api_bicimad.env'
path_data_stations = 'https://openapi.emtmadrid.es/v1/transport/bicimad/stations'
names_stations = []
bicis = []

def email(env_file):
    load_dotenv(env_file)
    email = os.environ.get("email")
    return email

def password(env_file):
    load_dotenv(env_file)
    password = os.environ.get("password")
    return password

def api_bicimad_connection(path_api, email, password):
    response = requests.get(path_api,headers={"email": email, 'password' : password})
    json_api_data = response.json()
    return json_api_data

def access_token(json_api_data):
    token = json_api_data['data'][0]['accessToken']
    return token

def get_data_stations(path_data_stations, token):
    response = requests.get(path_data_stations,headers={'accessToken': token })
    json_data_stations = response.json()
    return json_data_stations

def data_bicis_stations(name_stations, bicis, json_data_stations):
    for i in range(len(json_data_stations['data'])):
        name = json_data_stations['data'][i]['name']
        bicicletas = str(json_data_stations['data'][i]['dock_bikes'])
        name_stations.append(name)
        bicis.append(bicicletas)
    return name_stations, bicis

def dataframe_bicis(name_stations, bicis): 
    dataframe_bicis = pd.DataFrame(list(zip(name_stations, bicis)),columns =['Bicimad station', 'bikes available'])
    return dataframe_bicis

def dataframe_bicis_merged(dataframe_embajadas_bicimad, dataframe_bicis):
    dataframe_all = dataframe_embajadas_bicimad.merge(dataframe_bicis, how = 'inner' , on = 'Bicimad station')
    return dataframe_all