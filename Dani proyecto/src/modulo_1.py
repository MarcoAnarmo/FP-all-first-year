'''
Created on 27 oct 2021

@author: Daniel Vela Camacho
'''
# -- coding: utf-8 --

import csv
from collections import namedtuple
from datetime import datetime 

Videogames = namedtuple("Videogames", "Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game")

####################################################################################################################################
def r_videogames(fichero):
    rows= []
    with open(fichero, encoding= "utf-8" ) as f:
        reader= csv.reader(f, delimiter = (";"))
        next(reader)
        for Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game in reader: 
            Date = datetime.strptime(Date, "%d/%m/%Y").date()
            if Multiplayer_Game == "true":
                Multiplayer_Game = True
            elif Multiplayer_Game == "false":
                Multiplayer_Game = False
            
            tupla = Videogames(int(Rank), Name, Platform, Date , Genre ,Publisher,  float(Global_Sales), Multiplayer_Game)
            rows.append(tupla)
    return print (rows)
    
    
r_videogames(r"../data/vgsales.csv")
"""
pene= r_videogames(r"../data/vgsales.csv")

for i in range (5):
        print(pene[i])
        
print(len(pene))
"""