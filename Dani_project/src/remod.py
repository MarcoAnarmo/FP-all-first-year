'''
Created on 23 dic 2021

@author: danie
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
            
            games = v(int(Rank), Name, Platform, Date , Genre ,Publisher,  float(Global_Sales), Multiplayer_Game)
            videogames.append(games)
    return videogames

def f_platform(platform):
    filteredgames =[v.Name for v in v if v.Platform == platform   ]
    return filteredgames 
def calculate_platformsells(platform):
    platformsells = [(v.Global_Sales) for v in v if v.Platform == platform]
    average_sells = sum(platformsells)/len(platformsells)
    return average_sells
def maxsellsplatform(platform,multiplayergame):
    f = [(v.Name, v.Global_Sales) for v in v if platform == v.Platform and multiplayergame == v.Multiplayer_Game]
    f.sort(key = lambda x: x[1])
    return f 
def datefiltered(platform ):
    d =[(v.Name, v.Date) for v in v if v.Platform == platform]
    d.sort(key = lambda x: x[1])
    return d 
def platformdictionary(platform ):
    g = [v.Genre for v in v if platform == v.Platform]
    d=Counter(g)
    return(d)
#ENTREGA 3 
def dictionary_plat():
    p = [v.Platform for v in v ]
    d = Counter(p)
    return d 
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
def maxsells():
    aux= aux_sells(v)
    max_key = max(aux.items(), key=operator.itemgetter(1))[0]
    sells= aux[max_key]
    return (max_key, sells)
def percentagesells():
    percentages = list()
    aux = aux_sells()
    v = aux.values()
    k = aux.keys()
    t = sum(v)
    for v in v:
        p=(v/t)*100
        percentages.append(p)
    result = dict(zip(k,percentages))
    return result
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
    
