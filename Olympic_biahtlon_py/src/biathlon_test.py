'''
Created on 27 oct 2021

@author: macdemarco
'''
from biathlon import *

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
"""
        La función main de esta entrega llama a la función lee_fichero definida en el biathlon con la que conseguimos una
        lista de tuplas de este mismo fichero y devuelve por pantalla:
            - la longitud de la lista de tuplas
            - sus primeros 5 valores.
        
"""
def main_entrega1 ():
        
        print ("################ ENTREGA 1 ################\n")
        
        
        lista_tuplas = lee_biathlon("../data/olympic_biathlon.csv")
        
        print ("La lista de tuplas BIATHLON tiene una longitud de", len(lista_tuplas), "filas.\n")
        
        
        for i in range(5):
            
            print (f"El valor {i} de la tupla es:", lista_tuplas[i])
pass

main_entrega1()

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 2
#----------------------------------------------------------------------------------------------------------------------------
"""
        La función main de esta entrega llama a la función lee_biathlon definida en lee_biathlon con la que conseguimos una
        lista de tuplas de un fichero csv, la llamaremos Biathlon.
        
        En el primer bloque de la entrega obtenemos:
        
            -El filtrado de los ganadores en Biathlon:
                - cuantos ganadores hay en la tupla.
                - los primeros 3 ganadores que aparecen en la la lista de tuplas.
            
            -El cálculo de la media de todos los tiempos olímpicos en las diferentes pruebas del biathlon.
        
        En el segundo bloque de la entrega obtenemos:
            
            -El cálculo del mejor resultado registrado en la lista de tuplas Biathlon (al no coincidir ningún resultado
            con la característica de ser máximo, la función tan solo devuelve uno).
            
            -Todos los registros filtrados por nacionalidad y que se encuentran ordenados en función a la disciplina registrada.
            
            -Un diccionario en el que la clave registra la nacionalidad y el valor indica la cantidad de veces que se ha
            registrado dicha nacionalidad.
        
"""
def main_entrega2 ():
        
        
        print ("\n################ ENTREGA 2 ################\n")
        
        print ("________________ BLOQUE I _________________\n")
        
        
        biathlon = lee_biathlon("../data/olympic_biathlon.csv")
        
        ganadores = filtra_ganador(biathlon)
        
        print("*** Función filtra_ganador ***\n")
        
        print ("Han habido", len(ganadores), "ganadores registrados en Biathlon.\n")
        
        
        for i in range(3):
            
            print (f"El ganador número {i} de la tupla GANADORES, es:", ganadores[i])
            
        
        print("\n*** Función calcula_media_de_resultados_olímpicos ***\n")
        
        print ("El tiempo medio de todos los resultados olímpicos es de", calcula_media_de_resultados_olímpicos(biathlon), "segundos.\n")
        
        
        print ("________________ BLOQUE II ________________\n")
        
        print("*** Función obtener_registro_mejor_resultado ***\n")
        
        print("El mejor resultado regitrado en Biathlon, es:\n", obtener_registro_mejor_resultado(biathlon))
        
        print("\n*** Función obtener_registro_por_nacionalidad ***\n")
        
        print("Los registros por nacionalidad ordenados en función de la disciplina:\n", obtener_registro_por_nacionalidad(biathlon))
        
        print("\n*** Función agrupar_por_nacionalidades_registradas ***\n")
        
        print("La clave es la nacionalidad y el valor cuántas veces se ha registrado esa nacionalidad:\n", agrupar_por_nacionalidades_registradas(biathlon))
        
pass

main_entrega2()

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------
"""
        La función main de esta entrega llama a la función lee_biathlon definida en lee_biathlon con la que conseguimos una
        lista de tuplas de un fichero csv, la llamaremos Biathlon.
        
        Crearemos 4 distintas funciones de las que mostramos por pantalla:
        
            -El contador de las diferentes disciplians registradas:
                - la clave es la disciplina.
                - el valor asociado cuántas veces se ha registrado dicha clave.
            
            -Una tupla de la forma (max_result, resultado) en la que mostramos:
                - max_result muestra la disciplina en la que se ha registrado el mayor resultado.
                - resultado muestra la mayor suma de todos los tiempos registrados en las diferentes disciplinas.
     
            -Un diccionario en el que:
                - las claves son las diferentes disciplinas registradas en Biathlon.
                - los valores son los porcentajes que corresponden a la suma de los tiempos en cada disciplina.
            
            -Un diccionario en el que:
                - las claves corresponden a cada una de las diferentes disciplinas registradas.
                - el valor muestra los 'n' primeros ganadores registrados en cada disciplina, ordenados alfabéticamente.
"""
def main_entrega3():
    
    print ("\n################ ENTREGA 3 ################\n")
    
    print ("________________ BLOQUE III _________________\n")
    
        
    biathlon = lee_biathlon("../data/olympic_biathlon.csv")
        
    print("*** Función contador_disciplina ***\n")
    
    print("La clave es la disciplina y el valor cuántas veces se ha registrado esa disciplina:\n", contador_disciplinas(biathlon))

    print("\n*** Función max_suma_result_por_disciplina ***\n")
    
    print("La mayor suma de los resultados registrada en una disciplina específica es:\n", max_suma_result_por_disciplina(biathlon), 
          "\n El primer objeto de la tupla es la disciplina en la que se ha registrado y el segundo valor es la suma de los tiempos en segundos.\n")
    
    print("*** Función porcentaje_resultados ***\n")
    
    print("La clave del diccionario es la disciplina y el valor es el porcentaje que correponde a la suma de los tiempos en dicha disciplina:\n", porcentaje_resultados(biathlon))
    
    print("\n*** Función ganador_por_disciplina ***\n")
    
    print("La clave corresponde a la disciplina y el valor muestra los 'n' primeros ganadores en esa disciplina ordenados alfabéticamente:\n", ganador_por_disciplina(biathlon))
    
    
    pass

main_entrega3()

def main_defensa():
    
    biathlon = lee_biathlon("../data/olympic_biathlon.csv")
        
    print("*** Función agrupar_por_nacionalidades_registradas_2 ***\n")
    
    print("El contador es:\n", agrupar_por_nacionalidades_registradas_2(biathlon))
    pass 

main_defensa()
    
