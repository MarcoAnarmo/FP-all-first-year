'''
Created on 29 nov 2021

@author: Daniel Vela Camacho
'''
# -- coding: utf-8 --
from modulo1 import * 
#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
def main_1():
    v = r_videogames(r"..\data\vgsales.csv")
    print("--------------------------ENTREGA 1--------------------------")
    print(f"Nuestro dataset tiene {len(v)} registros sobre videojuegos.")
    print ("Los primeros 5 registros de nuestro archivo .CSV son los siguientes:")
    for i in range(5):
        print(v[i])
 
def main2():
    print("--------------------------ENTREGA 2--------------------------")
    print("--------------------------BLOQUE 1 --------------------------")
    print("¿De que plataforma desea ver los 5 juegos más vendidos?")
    print("Puedes elegir entre las siguientes opciones:"
    "PSP, GB, SNES, XOne, PC, NES," 
    "GBA, XB, WiiU, PS4, N64, Wii, DS, X360, 3DS, PS, 2600, GC, GEN, PS3, PS2")
    value = input("¿Cuál es su decisión? Intente escribir la plataforma tal como aparece mencionada previamente: ")
    print(f"Los 5 juegos más vendidos en {value} son: ")
    v = r_videogames(r"..\data\vgsales.csv")
    filtradas = f_platform(value , v)
    for i in range(5):
        print(filtradas[i])
    answer = input("Ahora podrá ver la media de ventas en millones de una plataforma.¿Le interesa ver las ventas de la plataforma anteriormente elegida?")
    if answer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        sells =calculate_platformsells(value,v)
        print(f"La plataforma {value} ha obtenido {sells}  millones de ventas.")
    elif not answer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        value2 = input("¿De que plataforma le interesa ver las ventas? ")
        sells2 = calculate_platformsells(value2,v)
        print(f"La plataforma {value2} ha obtenido {sells2}  millones de ventas.")
    print("--------------------------BLOQUE 2 --------------------------")
    print("Ahora podrá ver los 5 juegos menos vendidos de una plataforma ,y ateniéndose al criterio de si el juego es multijugador.")
    value3 = input("¿Qué plataforma le interesa? ")
    multiplayer = input("¿Querrás ver juegos multijugador? ")
    if multiplayer == "si " or  "Si" or "Sí"  or "SÍ" or "sí" or "SI":
        multiplayer = True 
    else:
        multiplayer = False
    multiandplat =maxsellsplatform(value3, multiplayer,v)
    for i in range(5):
        print(multiandplat[i])
    print("Con la siguiente función podrá ver los 5 primeros juegos lanzados en una determinada plataforma")
    value4 = input("Introduce la plataforma a filtar: ")
    filtered = datefiltered(value4 ,v)
    print(f"Los 5 primeros juegos publicados en {value4} son: ")
    for i in range(5):
        print(filtered[i])
    print("La función a continuación, creará un diccionario donde se registrarán cuántos juegos hay de un determinado género de una plataforma determinada")
    value5 = input("Introduce la plataforma a filtrar: " ) 
    genresfiltered = platformdictionary(value5, v)
    print(f"En la plataforma {value5} tenemos los siguientes tipos de juegos: ")
    print(genresfiltered)

def main_2():
    print("--------------------------ENTREGA 2--------------------------")
    print("--------------------------BLOQUE 1 --------------------------")
    v = r_videogames(r"..\data\vgsales.csv")
    print("Los 5 juegos más vendidos en PS4 son: ")
    filtradas = f_platform("PS4" , v)
    for i in range(5):
        print(filtradas[i])
    sells2 = calculate_platformsells("PS4",v)
    print(f"La plataforma PS4 ha obtenido {sells2}  millones de ventas.")
    print("--------------------------BLOQUE 2 --------------------------")
    print("Ahora podrá ver los 5 juegos multijugador menos vendidos de la plataforma PS4. ")
    multiandplat =maxsellsplatform("PS4", True ,v)
    for i in range(5):
        print(multiandplat[i])
    print("Los 5 primeros juegos publicados en PS4 son: ")
    filtered = datefiltered("PS4" ,v)
    for i in range(5):
        print(filtered[i])   
    print("La función a continuación, creará un diccionario donde se registrarán cuántos juegos hay de un determinado género en la plataforma PS4.")  
    genresfiltered = platformdictionary("PS4", v)  
    print(genresfiltered) 
    
def main_3():    
    print("--------------------------ENTREGA 3--------------------------")
    print("Podrá ver un diccionario donde se almacenarán los géneros y de cuántos títulos dispone cada género.")
    v = r_videogames(r"..\data\vgsales.csv")
    dic1 = dictionary_plat(v)
    print(dic1)
    print("Ahora podrá visualizar que plataforma dispone de más ventas totales.")
    f2 = maxsells(v)
    print(f"La plataforma con más ventas es: {f2}.")
    f3 =percentagesells(v)
    print("Podrás ver un diccionario donde se almacenarán como claves las diversas plataformas, donde su correspondientes valores, serán el porcentaje de ventas  respecto el totalque supuso cada plataforma.")
    print(f3)
    f4 = gamespergenre(v,3)
    print("Ahora podrá ver un diccionario, donde las claves serán los diversos géneros, y los valores serán los n juegos más vendidos de dicho género. En este caso, se mostrarán los 3 juegos más vendidos.")
    print(f4)
    
main_1()
main_2()
main_3()
