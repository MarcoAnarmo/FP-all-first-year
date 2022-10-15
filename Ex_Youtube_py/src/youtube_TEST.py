# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:50:04 2019

@author: Toñi Reina
@Revisor: fermincruz, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

from youtube import *

def test_lee_trending_videos(videos):
    print("Leidos...", len(videos), "videos")
    print("Los tres primeros videos son:\n", videos[:3])
    print("Los tres últimos videos son:\n", videos[-3:])

#----------------------------------------------------------------------------------------------------------------------------

def test_media_visitas(videos):
    
    fecha_str= "15/11/2017"
    fecha1 = datetime.strptime(fecha_str,'%d/%m/%Y').date()
    print(f"La media de visitas del día {fecha_str} es", media_visitas(videos, fecha1))
    
    fecha_str= "11/1/2000"
    fecha2 = datetime.strptime(fecha_str,'%d/%m/%Y').date()
    print(f"La media de visitas del día {fecha_str} es", media_visitas(videos, fecha2))

#----------------------------------------------------------------------------------------------------------------------------

def test_video_mayor_ratio_likes_dislikes(videos):
    print("El video con mayor ratio es:\n", video_mayor_ratio_likes_dislikes(videos))
    
    print("El video con mayor ratio con la categoria Education es:\n", video_mayor_ratio_likes_dislikes(videos, 'Education'))
    
#----------------------------------------------------------------------------------------------------------------------------

def test_canales_top(videos):
    print("El top-3 de canales es:\n", canales_top(videos))
    print("El top-5 de canales es:\n", canales_top(videos, 5))

#----------------------------------------------------------------------------------------------------------------------------

def test_video_mas_likeability_por_categoria(videos):
    k=20
    print(f"Vídeo con más likeability por categoría con constante {k}\n", video_mas_likeability_por_categoria(videos))

#----------------------------------------------------------------------------------------------------------------------------

def test_incrementos_visitas(videos):
    pass   
 
#----------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    print("\nEJERCICIO 1")
    #haga aquí la lectura del fichero
    videos = lee_trending_videos("../data/ExYoutube.csv")
    test_lee_trending_videos(videos)
    
    print("\nEJERCICIO 2")  
    test_media_visitas(videos)
    print("\nEJERCICIO 3")  
    test_video_mayor_ratio_likes_dislikes(videos)
    print("\nEJERCICIO 4")  
    test_canales_top(videos)
    print("\nEJERCICIO 5")  
    test_video_mas_likeability_por_categoria(videos)
    print("\nEJERCICIO 6")  
    test_incrementos_visitas(videos)
