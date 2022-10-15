'''
Created on 27 oct 2021

@author: macdemarco
'''
import csv
from collections import namedtuple, Counter
from datetime   import datetime


Biathlon = namedtuple("Biathlon", "Country, Discipline, Gender, Host_city, Medal, Result, Winner, Date")

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------

def lee_biathlon(fichero):
    """
    Esta función devuelve una lista de tuplas correspondiente a los valores que recibe del fichero olympic_biathlon.csv en la carpeta data.
    Está preparada para devolver una lista de tuplas de la siguiente forma:
    ([str, str, boolean, str, int, float, str, datetime.date()])
    Como se observa está compuesta por 8 columnas con los siguientes valores:
        4 str
        1 int
        1 float
        1 boolean
        1 date
    """
    biathlon = []
    
    with open(fichero, encoding = "utf-8") as f:
        
        lector = csv.reader(f, delimiter = ";")
        
        next(lector)
        
        for Country, Discipline, Gender, Host_city, Medal, Result, Winner, Date in lector:
          
            # Transformamos los valores str a sus correspondientes valores
            
            Medal = int(Medal) 
            Result = float(Result)
            Date = datetime.strptime(Date, "%m/%d/%Y").date()
            
            if Gender == "Men":
                Gender = True
            else:
                Gender = False
                
            #Creamos una tupla con los datos de biathlon
            
            tupla = Biathlon(Country, Discipline, Gender, Host_city, Medal, Result, Winner, Date)
            
            #Añadimos la tupla a la lista biathlon
            
            biathlon.append(tupla)
            
    return biathlon

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 2
#----------------------------------------------------------------------------------------------------------------------------

#----BLOQUE I ---------------------------------------------------------------------------------------------------------------

def filtra_ganador(biathlon, podio= 1):
    """
    Esta función recibe una lista de tuplas y una posición de podio deseada que usaremos para filtrar los datos.
    Devuelve una lista por comprensión con la que obtenemos el nombre de los participantes que hayan quedado en el podio indicado
    en el argumanto de la función.
    """
    ganadores = [ t.Winner for t in biathlon if t.Medal == podio and 0 < podio <= 3]
    
    return ganadores

def calcula_media_de_resultados_olímpicos(biathlon):
    """
    Esta función recibe una lista de tuplas de la que extraemos una lista por comprensión con los diferentes registros de los resultados.
    Devuelve un float de la media de los resultados que se encuentran en la lista por comprensión obtenida.
    """
    resultados = [t.Result for t in biathlon]

    media_resultados = sum(resultados) / len(resultados)
    
    #Con el método format para strings podemos restringir la cantidad de decimales con la que queremos el resultado.
    media_resultados_4_decimales = "{0:.4f}".format(media_resultados) 
    
    return media_resultados_4_decimales

#----BLOQUE II ---------------------------------------------------------------------------------------------------------------

def obtener_registro_mejor_resultado(biathlon):
    """
    Esta función recibe una lista de tuplas de la que obtendremos el resultado máximo para posteriormente pasar un filtro con este valor
    y crear una lista de tuplas con todos los resultados que coincidadn con el máximo.
    """
    #Obtenemos el resultado máximo registrado en Biathlon.
    maximo = max(biathlon, key = lambda x:x.Result)
    
    resultado = [t for t in biathlon if t.Result == maximo.Result]
    
    return resultado 

def obtener_registro_por_nacionalidad(biathlon, pais = "ITA"):
    """
    Esta función recibe una cadena de tuplas y la abreviatura correspondiente al país por el que queremos filtrar nuestra lista.
    Obtenemos una lista con los registros que sean de la nacionalidad que coincida con la indicada. La ordenaremos con el método sort() 
    válido para listas. Se ordena en orden a las disciplinas registradas.
    """
    resultado = [ t for t in biathlon if t.Country == pais]
    
    resultado.sort()
    
    return resultado

def agrupar_por_nacionalidades_registradas(biathlon):
    """
    Esta función recibe una lista de tuplas de la que primeramente obtendremos una lista por comprensión con los registros de las diferentes
    nacionalidades de nuestro fichero.
    Crearemos un diccionario con esta lista por comprensión en el que las claves serán las diferentes nacionalidades registradas
    y el valor asociado será cuántas veces se han repetido estas nacionalidades.
    """
    nacionalidades_registradas= [t.Country for t in biathlon]
    agrupados= {}
    
    for nacionalidad in nacionalidades_registradas:
        if not nacionalidad in agrupados:
            agrupados[nacionalidad]=1
        else:
            agrupados[nacionalidad]= agrupados[nacionalidad] + 1
    return agrupados

def agrupar_por_nacionalidades_registradas_2(biathlon):
    
    nacionalidades_registradas= [t.Country for t in biathlon]
    agrupacion_nacionalidades_registradas = Counter(nacionalidades_registradas)
    
    return agrupacion_nacionalidades_registradas 


#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------
    
def contador_disciplinas(biathlon):
    """
    Esta función recibe una lista de tuplas de la que primeramente obtendremos una lista por comprensión con los registros de las diferentes
    disciplinas de nuestro fichero.
    Crearemos un diccionario con esta lista por comprensión en el que las claves serán las diferentes disciplinas registradas
    y el valor asociado será cuántas veces se ha repetido esta disciplina.
    """
    disciplinas_registradas = [t.Discipline for t in biathlon]
    contador_disciplinas = Counter(disciplinas_registradas)
    
    return contador_disciplinas

def max_suma_result_por_disciplina(biathlon):
    """
    Esta función recibe una lista de tuplas de la que primeramente obtendremos (a través de una función auxiliar) un diccionario al que se asociará
    a cada clave una disciplina registrada y el valor asociado será la suma de todos los tiempos registrados en esas disciplinas.
    Posteriormente se obtiene una tupla de la forma (disciplina,resultado) con la mayor suma de los tiempos registrados y para terminar se 
    muestra por pantalla la tupla (max_result, resultado) que muestra en primer lugar la disciplina en la que se ha encontrado la mayor suma y en
    lugar la mayor suma registrada. 
    """
    aux = aux_result(biathlon)
    
    max_result=max(aux.items(), key= lambda x: x[1])[0] #se obtiene una tupla de la forma (disciplina,resultado) con la mayor suma
    resultado = aux[max_result]
    return ( max_result, resultado)

def aux_result(biathlon):
    """
    Esta función auxiliar nos servirá para crear un diccionario a través de una lista de tuplas en el que las claves serán las diferentes disciplinas
    registradas y el valor asociado será la suma de todos los tiempos registrados en cada disciplina.
    Para terminar devuelve un diccionario en el que el valor de la suma se ha aproximado a 3 únicos decimales.
    """
    resultado_disciplina = [(t.Discipline, t.Result) for t in biathlon]
    dicc1={}
    dicc2={}
    for disciplina,resultado in resultado_disciplina:
        if not disciplina in dicc1:
            dicc1[disciplina]= resultado
        else:
            dicc1[disciplina] += resultado
            
    items = dicc1.items() 
    
    for k,v in items:
        v = round(v,3) #queremos 3 decimales
        dicc2[k] = v
        
    return dicc2 #obtenemos un diccionario con una disciplina como clave y una suma de los resultados como valor
        
def porcentaje_resultados(biathlon):
    """
    Esta función recibe una lista de tuplas del tipo biathlon y para comenzar crearemos una lista vacía en la que registraremos los porcentajes y
    llamamos de nuevo a la función auxiliar descrita con anterioreidad. Despues crearemos una variable del tipo lista con las claves del diccionario
    obtenido con la función auxiliar y otra de sus valores.
    Para terminar realizamos el porcentaje de cada valor registrado en la lista con los valores, lo añadimos a la lista porcentajesy redondeamos
    estos valores a 3 decimales exactos.
    Por último, devolvemos un diccionario en el que por el método zip hemos asociado a cada clave las diferentes disciplinas registradas
    y a cada valor su correspondiente porcentaje. 
    """
    porcentajes = []
    aux = aux_result(biathlon)
    claves = aux.keys()
    valores = aux.values()
    
    suma_valores = sum(valores)
    
    for valor in valores:
        porcentaje = (valor/suma_valores) * 100
        porcentajes.append(porcentaje)
        
    porcentajes_3_decimales = [round(t,3) for t in porcentajes] #asignamos 3 decimales a cada porcentaje en la lista porcentajes
       
    resultado = dict(zip(claves, porcentajes_3_decimales))
    return resultado

def ganador_por_disciplina(biathlon, n=3):
    """
    Esta función recibe una lista de tuplas del tipo biathlon y un número entero 'n' preestablecido con el valor 3.
    A través de un bucle 'for' creamos un diccionario al que asignamos a cada una de las diferentes disciplinas una tupla con todos los ganadores
    que se han registrado en ellas.
    Para terminar devolvemos un diccionario en el que ordenamos los valores (ganadores) alfabéticamente y nos quedamos con los 'n' primeros.
    """
    dicc = {}
    dicc1 = {}
    
    for t in biathlon:
        if not t.Discipline in dicc:
            disciplina_actual = t.Discipline
            dicc[disciplina_actual]= [t.Winner for t in biathlon if t.Discipline == disciplina_actual]
        
    items = dicc.items()
    
    for k,v in items:
        v = sorted(v[:n])
        dicc1[k] = v
    return dicc1
        
        
        
        
        
        
        
        
        
        
    