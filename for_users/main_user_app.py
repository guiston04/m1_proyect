
#import libraries

import argparse
import pandas as pd
import os

#Parameters
path = 'https://raw.githubusercontent.com/guiston04/m1_proyect/main/for_developers/files/df_embajadas_bicimad.csv'
path_google = 'https://raw.githubusercontent.com/guiston04/m1_proyect/main/for_developers/files/df_bicimad.csv'

# Script functions 

def bicimad_embajadas(path):
    df = pd.read_csv(path)
    return df
    

def bicimad_embajada_particular(embassy, path):
    df = pd.read_csv(path)
    #Resultado consulta usuario
    resultado = df[df["Place of interest"] == embassy] 
    return resultado

def file_creation():
    print(os.getcwd())
    #path_new_dir = os.path.join("./","files","results")
    path_new_dir = './results'
    if not os.path.exists(path_new_dir):
        os.mkdir(path_new_dir)
    return path_new_dir

def file_saving_one(path_new_dir, x, y, df):
    return df.to_csv(f'{path_new_dir}/{x}_de_{y}_bicimad.csv')

def file_saving_all(path_new_dir, df):
    return df.to_csv(f'{path_new_dir}/embassies_bicimad.csv')

def google_maps(resultado):
    location_resultado = resultado.iloc[0]['Bicimad station']
    list_station = location_resultado.replace(" ", "+")
    url = 'https://www.google.com/search?q='+'bicimad+' + list_station
    return url

# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Encontrar su bicimad station para diplomaticos' )
    help_message ='You have two options. Option 1: "all" get all the bicimads stations near to every embassies/consulates in madrid. Option 2: "one" get the nearest bicimad stations of the embassy/consulate of your choice' 
    parser.add_argument('-be', '--bicimadembassy', help=help_message, type=str)
    args = parser.parse_args()
    return args

# Pipeline execution

if __name__ == '__main__':
    path_new_dir = file_creation()
    if argument_parser().bicimadembassy == 'all':
        pip_result = bicimad_embajadas(path)
        file_saving_all(path_new_dir, pip_result)
    elif argument_parser().bicimadembassy == 'one':
        #Pregunta al usuario si filtro por una embajada consulado en particular
        x = input("Consulado o Embajada: ").lower().capitalize()
        y = input("Pais: ").lower().capitalize()
        embassy = x + " de " + y
        pip_result = bicimad_embajada_particular(embassy, path)
        file_saving_one(path_new_dir, x, y, pip_result)
        url = google_maps(pip_result)
        print(url)
    else:
        pip_result = 'FATAL ERROR...you need to select the correct method'
    print(f'result saved correctly at {os.getcwd()}')