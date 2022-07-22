# BICIMAD FOR DIPLOMATS

![alt text](https://www.bicimadgo.es/Imagenes/BcmGOTrans.aspx?width=754&height=158&ext=.png)

Hello everyone, and welcome to the app that is going to get diplomats in shape, reduce their stress and to avoid wars and make peace, as well as reduce their carbon dioxyde fingerprint!

# Status

This is the first version of the app.

# The app

This app has the objective to indicate what bicimad stations is the closest to your embassy or consulate. The result the user is going to get is a dataframe with the embassy/consulate that has been selected, its nearest bicimad station, and the available number of bikes left to use!

The objective is to incentivize this transportation method in the city of madrid but also to get diplomats to their crucial meetings in time as well as giving them a time to do some exercice!

# The logic behind

In order to give the user this result, the application is using and crossing information from two separate databases: Ironhack database of embassies and consulates in Madrid and Bicimad Stations database from Madrid city council.

# Two apps for two kind of users

This app has been developped using python 3.9.

To use the following application you will need different libraries, but developers and users will have different needs. These are described in the following lists:

USERS: 

Pandas `import pandas as pd`\
OS `import os`\
Argparse `import argparse`

DEVELOPERS:

Sqlalchemy `import sqlalchemy`\
Pandas `import pandas as pd`\
shapely.geometry `from shapely.geometry import Point`\
geopandas `import geopandas as gpd`\
requests `import requests`

# Usage

In order to use both apps, you'll need to have all the libraries described before installed. Once you installed them, you'll just need to clone this repository or download the folders you are interested in (for_users, for_developers or both).

Once downloaded, the USER app will need one parameter to run correctly.
They are two possibilities:

`python main_user_app.py -be one`

This would be use in case you are looking for the nearest bicimad station from a particular embassy or consulate.\
This will ask the user for two inputs.\
First : Embassy or Consulate\
Second : Country\
Result: Dataframe with info on the nearest bicimad station, URL to get faster to google maps and the number of bikes that are available for use.
The dataframe will be saved in folder that will create itself when running the script. The path to get to it will be informed with the result of the command.

`python main_user_app.py -be all`

This would be use in case you are looking for the nearest bicimad station from a all embassies or consulates in Madrid.\
This will ask the user for no inputs.\
Result: Dataframe with info on the nearest bicimad station.
The dataframe will be saved in folder that will create itself when running the script. The path to get to it will be informed with the result of the command.

# Files

for_developers\
------| bicimad_refact\
--------------| bicimad_refact.py\
------| embajadas_bicimad_refact\
--------------| embajadas_bicimad_refact.py\
------| embajadas_refact\
--------------| embajadas_refact.py\
------| files\
--------------| df_bicimad.csv\
--------------| df_consulados_embajadas.csv\
--------------| df_embajadas_bicimad.csv\

for_users\
------| main_user_app.py\


# Coming soon

Automate the pipeline of the back end of the developer app.\
URL that directly goes to google maps.\








