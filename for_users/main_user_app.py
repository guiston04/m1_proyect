
#import libraries

import argparse
import pandas as pd


# Script functions 

def bicimad_embajadas():
    df = pd.read_csv('https://raw.githubusercontent.com/guiston04/proyecto_m1/main/dataframes/df_embajadas_bicimad.csv')
    return df
    

def bicimad_embajada_particular(embassy):
    df = pd.read_csv('https://raw.githubusercontent.com/guiston04/proyecto_m1/main/dataframes/df_embajadas_bicimad.csv')
    #Resultado consulta usuario
    resultado = df[df["Place of interest"] == embassy] 
    return resultado
    

# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Encontrar su bicimad station para diplomaticos' )
    help_message ='You have two options. Option 1: "all" get all the bicimads stations near to every embassies/consulates in madrid. Option 2: "one" get the nearest bicimad stations of the embassy/consulate of your choice' 
    parser.add_argument('-be', '--bicimadembassy', help=help_message, type=str)
    args = parser.parse_args()
    return args

# Pipeline execution

if __name__ == '__main__':
    if argument_parser().bicimadembassy == 'all':
        pip_result = bicimad_embajadas()
    elif argument_parser().bicimadembassy == 'one':
        #Pregunta al usuario si filtro por una embajada consulado en particular
        x = input("consulado o embajada: ")
        y = input("pais: ")
        embassy = x + " de " + y
        pip_result = bicimad_embajada_particular(embassy)
    else:
        pip_result = 'FATAL ERROR...you need to select the correct method'
    print(pip_result)