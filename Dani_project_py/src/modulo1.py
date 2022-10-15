'''
Created on 23 dic 2021

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
import operator
from collections import defaultdict

v = namedtuple("v", "Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game")
#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------

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
            games = v(int(Rank), Name, Platform, Date , Genre ,Publisher,  float(Global_Sales), Multiplayer_Game)
            videogames.append(games)
    return videogames
''' 
En esta primera función,recibirá como entrada el archivo .csv a leer. Donde se almacenarán los datos contenidos en una lista de tuplas 
de tipo Videogames, para ello usaremos la librería que incluye las "namedtuples" para facilitar el trabajo con dichos datos. Recordar el 
uso de "delimiter= ;" en la lectura del .csv para determinar que la lectura de distintos datos vendrá dado por ese carácter.
Se deben de transfomar los datos incluidos en dicho .csv según su tipo, ya sea int,float, o en el caso de que sea una fecha, usaremos la librería datetime
para el correspondiente trata de fechas. 
        ENTRADA = "Archivo .csv a leer" 
               -> "str"
        SALIDA = "Lista de tuplas con la información del .csv"
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
def f_platform(platform,v):
    filteredgames =[v.Name for v in v if v.Platform == platform]
    return filteredgames
''' 
Esta funcion se encargará de devolver los 5 juegos más vendidos de una determinada plataforma, según el interés del usuario.
        ENTRADA = "Plataforma sobre la que obtener los 5 juegos más vendidos , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA  = Lista con los 5 juegos más vendidos de la plataforma indicada.
                -> ["str", "str", "str", "str" , "str"]
'''
def calculate_platformsells(platform,v):
    platformsells = [(v.Global_Sales) for v in v if v.Platform == platform]
    average_sells = round(sum(platformsells)/len(platformsells),3)
    return average_sells
''' 
Esta funcion se encargará de devolver la venta media (en millones) de una determinada plataforma. Utilizaremos funcion built-in, como sum() y len() para facilitar dichos cálculos.
Además usaremos round() para dar el resultado numérico con un numero específico de decimales
        ENTRADA = "Plataforma sobre la que obtener la media de ventas  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA  = Número de ventas (en millones)
                -> "float"
''' 
#----- BLOQUE 2 -------------------------------------------------------------------------------------------------------------     
def maxsellsplatform(platform,multiplayergame,v):
    f = [(v.Name, v.Global_Sales) for v in v if platform == v.Platform and multiplayergame == v.Multiplayer_Game]
    f.sort(key = lambda x: x[1])
    return f
'''
Esta funcion se encargará de devolver los 5 juegos menos vendidos de una plataforma, ateniéndose si dichos títulos disponen de modalidad multijugador. 
Para realizar la ordenación de los juegos menos vendidos utilizaremos el metodo .sort() e indicando que los juegos se ordenen con el criterio del 2 elemento de la tupla, es decir la venta de dicho juego,
y los ordenará de menor a mayor.
        ENTRADA = "Plataforma sobre la que obtener los juegos menos vendidos"  ,"Criterio de si el juego es multijugador o no "Lista de tuplas con la información dataset" (platform,multiplayergame, v)
                -> "str", boolean,  [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Lista de tuplas con los 5 juegos menos vendidos de una determinanada plataforma, segun sean multijugador o no. (Nombre del juego, Ventas)
                -> [("str","float"),("str","float"),("str","float"),("str","float"),("str","float")]
'''
def datefiltered(platform,v ):
    d =[(v.Name, v.Date) for v in v if v.Platform == platform]
    d.sort(key = lambda x: x[1])
    return d 
'''
Esta función se encargará de devolver los 5  primeros juegos publicados  de una determinada plataforma  (más antigüos primero). De nuevo recurriremos al método .sort() y dando como clave de ordenación,
el 2 elemento de la tupla, es decir su fecha de lanzamiento, obteniéndose así los juegos ordenados cronológicamente.
        ENTRADA = "Plataforma sobre la que obtener los 5 primeros juegos lanzados"  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str",[Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Lista de tuplas con los 5 juegos lanzados en la plataforma especificada (Nombre del juego,Fecha de lanzamiento)
                -> [("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),]
'''
def platformdictionary(platform ,v):
    g = [v.Genre for v in v if platform == v.Platform]
    d=Counter(g)
    return(d)
'''
Esta función se encargará de contabilizar cuántos juegos hay disponibles de los diversos géneros en una plataforma específica. Para ello, realizaremos un diccionario 
donde cada clave será cada tipo de género, y su valor, el número de juegos de ese género en esa determinada plataforma. Para facilitar la creación de dicho diccionario, usaremos la librería "Counter"
que se encargará de contar cuantas veces aparece un género en una determinada plataforma.
        ENTRADA = "Plataforma sobre la que obtener la cantidad de juegos de cada género  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan la cantidad de juegos de cada género.
                -> {género1("str"):valor1("int"),género2("str"):valor2("int")...}
        
'''
#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------
def dictionary_plat(v):
    p = [v.Platform for v in v ]
    d = Counter(p)
    return d 
''' 
Esta función devolverá un diccionario donde se enumerarán cuántos juegos de cada plataforma están en el TOP 500 juegos más vendidos de todos los tiempos.De nuevo para llevar a cabo dicho diccionario, recurriremos a la 
librería "Counter", para contabilizar cuantas veces aparece cada plataforma en el dataset.
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan la cantidad de juegos de cada plataforma
                -> {plataforma1("str"):valor1("int"),plataforma2("str"):valor2("int")...}
               
 
'''
def aux_sells(v):
    s = [(v.Platform, v.Global_Sales) for v in v ]
    d = {}
    d1= {}
    for p,g in s:
        if not p in d:
            d[p]= g
        else:
            d[p] += g
    items = d.items()
    for k,v in items:
        v = round(v,3)
        d1[k] = v
    return d1
''' 
Esta función auxiliar (la utilizaremos en la funcion maxsells(v)) devolverá un diccionario donde se contabilizarán las ventas de juegos de una determinada plataforma.Siendo las claves las plataformas, y los valores sus correspondientes ventas totales.
En este caso, llevaremos a cabo la creación de dicho diccionario de la manera tradicional, a través de un bucle. El segundo bucle esta llevado a cabo para mostrar el valor de las ventas con un determinado número de
de decimales, en este caso 3, todo ello para facilitar la visualización del contenido del diccionario. 
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan las ventas de juegos de cada plataforma
                -> {plataforma1("str"):valor1("float"),plataforma2("str"):valor2("float")...} 
'''
def maxsells(v):
    aux= aux_sells(v)
    max_key = max(aux.items(), key=operator.itemgetter(1))[0]
    sells= aux[max_key]
    return (max_key, sells)
''' 
Esta función se encargará de sacar la plataforma con más ventas, utilizando como ayuda la funcion auxiliar (aux_sells(v)). En este caso esta función determinará la clave-valor , con el valor mas elevado,
del diccionario creado por la función auxiliar. Para ello utilizaremos la librería "Operator" que nos permitirá encontrar dicho clave-valor.
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Clave-Valor (Platforma-Ventas totales), con las  mayores Ventas Totales 
                -> Clave("str) - Valor("flaot")
'''
def percentagesells(v):
    percentages = list()
    aux = aux_sells(v)
    v = aux.values()
    k = aux.keys()
    t = sum(v)
    for v in v:
        p=(v/t)*100
        percentages.append(p)
    result = dict(zip(k,percentages))
    return result
''' 
En esta funcion de nuevo recurriremos a la funcion auxiliar de (aux_sells(v)) para hacer un nuevo diccionario donde se registren nuevos clave-valor, donde cada clave es cada plataforma.
Dichas claves corresponden al porcentaje de ventas que supusieron respecto el total de ventas. 
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan que porcentaje de ventas respecto el total que supuso cada plataforma. 
                -> {plataforma1("str"):porcentaje1("float"),plataforma2("str"):porcentaje2("float")...} 
'''
def gamespergenre(v,n):
    d = defaultdict(list)
    d1 = {}
    for v in v:
        d[v.Genre].append(v.Name)
    items = d.items()
    for k,v in items:
        v = v[:n]
        d1[k] = v
    return d1 
''' 
Esta función creará un diccionario donde se mostrarán como claves los diversos géneros y los valores serán una lista con los juegos más vendidos de ese determinado género. Para llevar a cabo 
la creación de dicho diccionario recurriremos a la librería "Defaultdict" para facilitar el proceso. Donde se indicarán que los valores serán las listas con los juegos más vendidos.
La creacion del diccionario vacío "d1" será utilizado para volcar los datos creados por la librería "Defaultdict" tras realizar un slicing, para mostrar los "n" juegos más vendidos de un género.
Siendo "n" el numero de juegos a mostrar.  
        ENTRADA =  "Lista de tuplas con la información dataset", Número de juegos a mostrar en los valores del diccionario (v,n)
                -> [Videogames(int,str,str,date,str,str,float,boolean)], "int"
        SALIDA = Diccionario donde se recopilan los "n" juegos más vendidos de todos los géneros.
                -> {género1("str"):[juego1,juego2...juego"n"("str","str","str")],género2("str"):[juego1,juego2...juego"n"("str","str","str")]}
'''

