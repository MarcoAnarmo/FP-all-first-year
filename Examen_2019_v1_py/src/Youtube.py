# -*- endoing utf-8 -*-
'''
Created on 25 ene 2022

@author: macdemarco
'''

#Importaciones
import csv
from datetime import datetime
from collections import namedtuple, Counter
from pickle import NONE
from tornado.test.util_test import ReUnescapeTest

Video = namedtuple('Videos', 'id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

#Funciones

# Ejercico 1)

def lee_trending_videos(fichero):
    lista = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            fecha_trending = datetime.strptime(fecha_trending, '%d/%m/%Y').date()
            visitas,likes,dislikes = int(visitas),int(likes),int(dislikes)
            
            tupla = Video(id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes)
            
            lista.append(tupla)
            
        return lista
    
# Ejercicio 2)

def media_visitas(Video, fecha):
      
    fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
    visita = [e.visitas for e in Video if fecha == e.fecha_trending]
    
    if len(visita) == 0:
        
        media_visitas = 0
    else:
        media_visitas = sum(visita) / len(visita)
    
    return media_visitas

# Ejercicio 3)

def video_mayor_ratio_likes_dislikes(Video, categoria = None):
    '''
    Input: lista de tuplas del tipo Video y categoria predefinida por None.
    Output: tupla de tipo Video de la categoría dada como parámetro que ha tenido una mayor ratio likes/dislikes.
    '''
    res = [video for video in Video if (categoria == None or categoria == video.categoria) and video.dislikes > 0]
    
    return max(res, key = lambda x:x.likes/x.dislikes)


# Ejercico 4)

def canales_top(Video, n = 3):
    
    res = Counter(e.canal for e in Video)
    res = sorted(res.items(), key = lambda x:x[1], reverse = True)
    
    return res[:n]

# Ejercicio 5)

def video_mas_likeability_por_categoria(Video, k = 20):
    #diccionario categoria:tuplas_videos
    res = dict()
    for e in Video:
        if e.categoria not in res:
            res[e.categoria] = [e]
        else:
            res[e.categoria].append(e)
    
    for categoria, tupla_videos in res.items():
        maximo = max(tupla_videos, key = lambda video:likeability(video, k)) #obtener máximo de los videos
        res[categoria] = maximo.id #asocias a la clave la id del video con más likeability
        
    return res


def likeability(Video, k):
    return ((Video.likes * k)-Video.dislikes)/(k* Video.visitas)
    
# Ejercicio 6)

def incremento_visitas(Video, canal):
    
    dias = {e.fecha_trending for e in Video}
    dias = sorted(dias)
    dicc = visitas_por_dia(Video)
    
    contador=[]
    for x in range(len(dias) - 1):
        incremento = dicc.get(dias[x+1], 0) - dicc.get(dias[x], 0)
        contador.append(incremento)
    return contador
    
    
def visitas_por_dia(Video):
    res = dict()
    for e in Video:
        if e.fecha_trending not in res:
            res[e.fecha_trending] = e.visitas
        else:
            res[e.fecha_trending] += e.visitas
            
    return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    