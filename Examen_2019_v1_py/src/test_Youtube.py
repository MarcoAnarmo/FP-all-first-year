'''
Created on 25 ene 2022

@author: macdemarco
'''
from Youtube import *

def test_lee_trending_videos():
    print('\n------------------------------------------------------------------------\n')
    
    lista_tupla = lee_trending_videos('../data/MX_Youtube_2017_utf8.csv')
    print(lista_tupla[:3])

def test_media_visitas():
    print('\n------------------------------------------------------------------------\n')
    lista_tupla = lee_trending_videos('../data/MX_Youtube_2017_utf8.csv')
    
    res = media_visitas(lista_tupla, '11/01/2017')
    print(res)

def test_video_mayor_ratio_likes_dislikes():
    print('\n------------------------------------------------------------------------\n')
    lista_tupla = lee_trending_videos('../data/MX_Youtube_2017_utf8.csv')
    
    print("El video con mayor ratio es:\n", video_mayor_ratio_likes_dislikes(lista_tupla))
    
    print("El video con mayor ratio de la categoria Education es:\n", video_mayor_ratio_likes_dislikes(lista_tupla, 'Education'))
    
def test_canales_top():
    print('\n------------------------------------------------------------------------\n')
    lista_tupla = lee_trending_videos('../data/MX_Youtube_2017_utf8.csv')
    
    print('El top 3 de canales es: \n', canales_top(lista_tupla))
    print('El top 5 de canales es: \n', canales_top(lista_tupla, 5))
    
def test_video_mas_likeability_por_categoria():
    print('\n------------------------------------------------------------------------\n')
    lista_tupla = lee_trending_videos('../data/MX_Youtube_2017_utf8.csv')
    
    res = video_mas_likeability_por_categoria(lista_tupla)
    print('Vídeo con más likeability por categoría con constante 20:')
    
    for x,y in res.items():
        print(x, '----->', y)
    
    
if __name__ == '__main__':
    test_lee_trending_videos()
    test_media_visitas()
    test_video_mayor_ratio_likes_dislikes()
    test_canales_top()
    test_video_mas_likeability_por_categoria()