
#Import libraries

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd

#creation del objeto engine para acceder a datos de BiciMad
def engine(connection_string):
    engine = create_engine(connection_string)
    return engine

#Definición de funciones que aplicar sobre columna geometry.coordinates

def latitudes(x):
    x = x.replace("[","").replace("]","")
    x = x.split(",")
    return x[0]

def longitudes(x):
    x = x.replace("[","").replace("]","")
    x = x.split(",")
    return x[1]
