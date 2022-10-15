'''
Created on 14 dic 2021

@author: macdemarco
'''
import csv
from collections import namedtuple
from datetime import datetime, date
from collections import Counter

Video = namedtuple('Video', 'id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

#----------------------------------------------------------------------------------------------------------------------------

def lee_trending_videos(fichero):
    
    with open (fichero, encoding="utf-8") as f:
        
        lector = csv.reader(f, delimiter= ";")
        next(lector)
        res=[]
        
        for id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            
            tupla=Video(id_video, datetime.strptime(fecha_trending,'%d/%m/%Y').date(), titulo, canal, categoria, 
                        int(visitas), int(likes), int(dislikes))
            
            res.append(tupla)
            
    return res

#----------------------------------------------------------------------------------------------------------------------------

def media_visitas(videos, fecha):
    
    visitas = [ t.visitas for t in videos if t.fecha_trending == fecha ]
    media = 0
    
    if len(visitas) > 0:

        media = sum(visitas) / len(visitas)
    
    return media

#----------------------------------------------------------------------------------------------------------------------------

def video_mayor_ratio_likes_dislikes(videos, categoria=None):
    
    videos = [video for video in videos 
              if (categoria == None or categoria == video.categoria) and video.dislikes > 0]
    
    return max(videos, key=lambda video : video.likes / video.dislikes)

#----------------------------------------------------------------------------------------------------------------------------

def videos_por_canal(videos):
    
    res = dict()
    for video in videos:
        
        if video.canal in res:
            res[video.canal] += 1;
        
        else:
            res[video.canal] = 1
            
    return res

def canales_top(videos, n=3):
    
    dicc = videos_por_canal(videos)
    
    return sorted(dicc.items(), key=lambda item:item[1], reverse=True)[:n]

#----------------------------------------------------------------------------------------------------------------------------

def video_mas_likeability_por_categoria(videos, k=20):
    
    dicc = videos_por_categoria(videos)
    res= dict()
    for categoria, lista_videos in dicc.items():
        res[categoria] = max(lista_videos, key = lambda video:likeability(video, k))
        
    return res
def likeability(video,k):
    
    return ( k * video.likes - video.dislikes / (k * video.visitas))

def videos_por_categoria(videos):
    
    res = dict()
    for video in videos:
        
        if video.categoria in res:
            res[video.categoria].append(video)
        
        else:
            res[video.categoria] = [video]
            
    return res

#----------------------------------------------------------------------------------------------------------------------------

def incrementos_visitas(videos, canal):
    
    dias = dias_trending(videos)
    dicc = visitas_por_dia(videos,canal)
    incrementos = []
    for index in range(len(dias) - 1):
        incremento

















