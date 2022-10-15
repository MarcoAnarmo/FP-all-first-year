'''
Created on 29 nov 2021

@author: Daniel Vela Camacho
'''
'''
En este proyecto trabajaremos con los datos proporcionados con el dataset llamado "vgsales.csv", donde se almacenan datos de los 500 juegos más vendidos 
de todas las plataformas. Además, se incluye informacioón adicional, como la fecha de lanzamiento del videojuego, su género, su desarrolladora, las ventas 
globales de dicho juego y si dicho lanzamiento, incluye modo multijugador.

'''
# -- coding: utf-8 --
import csv
from collections import namedtuple
from datetime import datetime 
from collections import Counter

Videogames = namedtuple("Videogames", "Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game")


#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
'''
En esta primera entrega debemos de crear una función donde se lea el archivo .csv correspondiente y almacene todos los datos en una lista de tuplas, y 
su consecuente "función test" en el módulo1_test. Todo ello,con el fin de garantizar su adecuado funcionamiento.
'''
def r_videogames(file):   
    videogames= []
    with open(file, encoding= "utf-8" ) as f:
        reader= csv.reader(f, delimiter = (";"))
        next(reader)
        for Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game in reader: 
            Date = datetime.strptime(Date, "%d/%m/%Y").date()
            if Multiplayer_Game == "true":
                Multiplayer_Game = True
            elif Multiplayer_Game == "false":
                Multiplayer_Game = False
            
            games = Videogames(int(Rank), Name, Platform, Date , Genre ,Publisher,  float(Global_Sales), Multiplayer_Game)
            videogames.append(games)
    return videogames
''' 
En esta primera función,recibirá como entrada el archivo .csv a leer. Donde se almacenarán los datos contenidos en una lista de tuplas 
de tipo Videogames, para ello usaremos la librería que incluye las "namedtuples" para facilitar el trabajo con dichos datos. Recordar el 
uso de "delimiter= ;" en la lectura del .csv para determinar que la lectura de distintos datos vendrá dado por ese carácter.
Se deben de transfomar los datos incluidos en dicho .csv según su tipo, ya sea int,float, o en el caso de que sea una fecha, usaremos la librería datetime
para el correspondiente trata de fechas. 
        ENTRADA= "Archivo .csv a leer" 
                -> "str"
        SALIDA= "Lista de tuplas con la información del .csv"
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
'''

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 2
#----------------------------------------------------------------------------------------------------------------------------
''' 
En esta segunda entrega se agruparán las funciones en dos bloques separados, donde en ambos bloques encontraremos funciones, que llevarán
a cabo una determinada función de filtro según el interés del usuario.
'''

#----- BLOQUE 1 -------------------------------------------------------------------------------------------------------------
def f_platform(platform,games):
    platformfilter = [(Name) for _,Name, Platform, _,_, _, _,_, in games 
                    if platform == Platform ]
    return platformfilter
'''
Esta función recibirá como parámetros formales, "platform" y "games". Siendo dichos elementos "platform",  la  plataforma  de la que
deseamos obtener los juegos más vendidos y "games" ,la lista de tuplas obtenida en la funcion "r_videogames".
            ENTRADAS=
                -> platform = str
                -> games = Lisa  de tuplas 
            SALIDA= 
                -> Lista de juegos de la plataforma definida en la entrada
'''

def calculate_platformsells(platform,games):
    platformsells = [(Global_Sales) for  _,_, Platform, _,_, _, Global_Sales ,_ in games
                     if platform == Platform]
    averageplatformsells = sum(platformsells)/len(platformsells)
    return averageplatformsells

#----- BLOQUE 2 -------------------------------------------------------------------------------------------------------------

def maxsellsplatform(platform,multiplayergame,games):
    maxsellsplatform =  [(Name, Global_Sales) for  _,Name, Platform, _,_, _, Global_Sales, Multiplayer_Game in games
                     if platform==Platform and multiplayergame == Multiplayer_Game  ]
    maxsellsplatform.sort(key = lambda x: x[1])
    return maxsellsplatform 


def datefiltered(platform, games):
    datefiltered =  [(Name, Date ) for  _,Name, Platform, Date,_, _,_, _ in games
                     if platform==Platform ]
    datefiltered.sort(key = lambda x: x[1])
    return datefiltered

def platformdictionary(platform, games):
    filteredplatform= {}
    platform = [(Genre) for _,_, Platform, _,Genre, _, _,_, in games 
                    if platform == Platform ]
    for i in platform:
        if not i in filteredplatform:
            filteredplatform[i]=1
        else:
            filteredplatform[i]= filteredplatform[i] + 1 
    return filteredplatform   

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------



''' 
1 funcion:  que te saque cuantos juegos tiene las plataforma, segun el año ? 

2 funcion: diccionario que almacene las ventas totales de las plataformas , y sauqe el maximo 
3 funcion tipo 13: que saque el porcentaje de ventas que supusieron una determinada plataforma respecto el total:
funcion 4 : usando la funcion anterior sacar una lista que ordene las claves de los porcentajes almacenados de manera progresiva. 

'''
def dictionary_plat(games):
    platdict = {}
    platform = [(Platform) for _,_, Platform, _,_, _, _,_ in games  ]
    for i in platform:
        if not i in platdict:
            platdict[i]=1
        else:
            platdict[i]= platdict[i] + 1 
    return platdict   
def max_sells(games):
    sellsdict = {}
    sellsandplat = [(Platform,Global_Sales) for  _,_, Platform, _,_, _, Global_Sales,_ in games ]
    return sellsandplat
    



