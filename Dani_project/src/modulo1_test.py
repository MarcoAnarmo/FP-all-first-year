'''
Created on 29 nov 2021

@author: Daniel Vela Camacho
'''
# -- coding: utf-8 --
from modulo1 import * 
#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
def main1():
    games = r_videogames(r"C:\eclipse\WSPython\Videogames Sales\data\vgsales.csv")
    print("--------------------------ENTREGA 1--------------------------")
    print(f"Nuestro dataset tiene {len(games)} registros sobre videojuegos.")
    print ("Los primeros 5 registros de nuestro archivo .CSV son los siguientes:")
    for i in range(5):
        print(games[i])
 
def main2():
    print("--------------------------ENTREGA 2--------------------------")
    print("--------------------------BLOQUE 1 --------------------------")
    print("¿De que plataforma desea ver los 5 juegos más vendidos?")
    print("Puedes elegir entre las siguientes opciones:"
    "PSP, GB, SNES, XOne, PC, NES," 
    "GBA, XB, WiiU, PS4, N64, Wii, DS, X360, 3DS, PS, 2600, GC, GEN, PS3, PS2")
    value = input("¿Cuál es su decisión? Intente escribir la plataforma tal como aparece mencionada previamente: ")
    print(f"Los 5 juegos más vendidos en {value} son: ")
    games = r_videogames(r"C:\eclipse\WSPython\Videogames Sales\data\vgsales.csv")
    filtradas = f_platform(value , games)
    for i in range(5):
        print(filtradas[i])
    answer = input("Ahora podrá ver la media de ventas en millones de una plataforma.¿Le interesa ver las ventas de la plataforma anteriormente elegida?")
    if answer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        sells =calculate_platformsells(value,games)
        print(f"La plataforma {value} ha obtenido {sells}  millones de ventas.")
    elif not answer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        value2 = input("¿De que plataforma le interesa ver las ventas? ")
        sells2 = calculate_platformsells(value2,games)
        print(f"La plataforma {value2} ha obtenido {sells2}  millones de ventas.")
    print("--------------------------BLOQUE 2 --------------------------")
    print("Ahora podrá ver los 5 juegos menos vendidos de una plataforma ,y ateniéndose al criterio de si el juego es multijugador.")
    value3 = input("¿Qué plataforma le interesa? ")
    multiplayer = input("¿Querrás ver juegos multijugador? ")
    if multiplayer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        multiplayer = True 
    else:
        multiplayer = False
    multiandplat =maxsellsplatform(value3, multiplayer,games)
    for i in range(5):
        print(multiandplat[i])
    print("Con la siguiente función podrá ver los 5 primeros juegos lanzados en una determinada plataforma")
    value4 = input("Introduce la plataforma a filtar: ")
    filtered = datefiltered(value4 ,games)
    print(f"Los 5 primeros juegos publicados en {value4} son: ")
    for i in range(5):
        print(filtered[i])
    print("La función a continuación, creará un diccionario donde se registrarán cuántos juegos hay de un determinado género de una plataforma determinada")
    value5 = input("Introduce la plataforma a filtrar: " ) 
    genresfiltered = platformdictionary(value5, games)
    print(f"En la plataforma {value5} tenemos los siguientes tipos de juegos: ")
    print(genresfiltered)

def main_2():
    print("--------------------------ENTREGA 2--------------------------")
    print("--------------------------BLOQUE 1 --------------------------")
    games = r_videogames(r"C:\eclipse\WSPython\Videogames Sales\data\vgsales.csv")
    print("Los 5 juegos más vendidos en PS4 son: ")
    filtradas = f_platform("PS4" , games)
    for i in range(5):
        print(filtradas[i])
    sells2 = calculate_platformsells("PS4",games)
    print(f"La plataforma PS4 ha obtenido {sells2}  millones de ventas.")
    print("--------------------------BLOQUE 2 --------------------------")
    print("Ahora podrá ver los 5 juegos multijugador menos vendidos de la plataforma PS4 ")
    multiandplat =maxsellsplatform("PS4", True ,games)
    for i in range(5):
        print(multiandplat[i])
    print("Los 5 primeros juegos publicados en PS4 son: ")
    filtered = datefiltered("PS4" ,games)
    for i in range(5):
        print(filtered[i])   
    print("La función a continuación, creará un diccionario donde se registrarán cuántos juegos hay de un determinado género en la plataforma PS4")  
    genresfiltered = platformdictionary("PS4", games)  
    print(genresfiltered) 
#main1()
main_2()   
    
    
def main3():
    games= r_videogames(r"C:\eclipse\WSPython\Videogames Sales\data\vgsales.csv")
    dictionary=dictionary_plat(games)    
    print(dictionary)
    ventas = max_sells(games)
    print(ventas)
    
#main3()    
    
    