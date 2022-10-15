# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:29:53 2020

@author: Damián Fernández
@revisor: Pepe Riquelme, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

import csv
from datetime import datetime
from collections import namedtuple, Counter

Compra = namedtuple('Compra','dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra')

def lee_compras(fichero):
    '''
    Lee un fichero de entrada en formato CSV y devuelve una lista de tuplas tipo Compra 
    conteniendo todos los datos almacenados en el fichero.    
    Use: datetime.strptime(cadena_fecha,'%d/%m/%Y %H:%M') para convertir una cadena a fecha/hora
    Entrada:
     - ruta: ruta del fichero csv que contiene los datos en codificación utf-8 
         -> str

    Salida:
     - compras: lista de tuplas con la información del fichero
         -> [Compra(str,str,str,datetime,datetime,float)]   
    '''
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida,total_compra in lector:
        
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M')
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M')
            total_compra = float(total_compra)
            res.append(Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra))
        
    return res


#----------------------------------------------------------------------------------------------------------------------------

def compra_maxima_minima_provincia(compras, provincia):
    '''
    Devuelve una tupla que contiene el importe máximo y el mínimo de las compras 
    que se han realizado en la provincia dada como parámetro. 
    Si la provincia toma el valor None, se devuelve una tupla con el 
    importe máximo y el mínimo calculados a partir de todas las compras
    Entrada:
     - compras: lista de tuplas con la información de compras
         -> [[Compra(str,str,str,datetime,datetime,float)]
     - provincia: nombre de la provincia -> str

    Salida:
     - tupla con el importe máximo y el mínimo.
         -> (float,float)
    '''
    compras_provincia = [compra for compra in compras
                         if provincia is None or compra.provincia == provincia] 
    maximo_compra = max(compras_provincia, key=lambda compra:compra.total_compra) 
    minimo_compra = min(compras_provincia, key=lambda compra:compra.total_compra)
    
    return (maximo_compra.total_compra, minimo_compra.total_compra)

#----------------------------------------------------------------------------------------------------------------------------

def hora_menos_afluencia(compras):
    '''
    Devuelve una tupla con la hora en la que llegan menos clientes y el número de 
    clientes que llegan a dicha hora. Recuerda que puedes acceder a la 
    hora de un objeto fecha/hora fh con fh.hour
    Entrada:
     - compras: lista de tuplas con la información de compras
         -> [[Compra(str,str,str,datetime,datetime,float)]
         
    Salida:
     - tupla con la hora con el mínimo número de llegadas 
       y el número de llegadas de dicha hora.
         -> (int,int)
    '''

    horas_llegadas = num_compras_por_hora(compras)
    return min(horas_llegadas.items(), key=lambda tupla: tupla[1])

#Función auxiliar: Creación de diccionario. Versión 1 
def num_compras_por_hora(compras):
    horas_llegadas = {}
    for compra in compras:
        if compra.fecha_llegada.hour not in horas_llegadas:
            horas_llegadas[compra.fecha_llegada.hour] = 1
        else:
            horas_llegadas[compra.fecha_llegada.hour] += 1
    return horas_llegadas
'''
#Función auxiliar: Creación de diccionario. Versión 2 
def num_compras_por_hora(compras):
    
    horas_llegadas = Counter(compra.fecha_llegada.hour for compra in compras)
    return horas_llegadas
'''
#----------------------------------------------------------------------------------------------------------------------------

def supermercados_mas_facturacion(compras, n=3): 
    '''
    Devuelve un ranking, es decir, una lista de tuplas 
    [(posición_ranking, (supermercado, facturacion))] con las n 
    marcas de supermercados que más facturan,
    en orden decreciente de facturación. 
    El ranking debe empezar por la posición 1
    Entrada:
     - compras: lista de tuplas con la información de compras
         -> [[Compra(str,str,str,datetime,datetime,float)]
     - n: número de marcas de supermercados a devolver -> int

    Salida:
     - Una lista de tuplas, cada una conteniendo:
       1) la posición en el ranking y 
       2) una tupla que contenga la marca del supermercado 
          y su facturación -> [(int,(str,float))]
    '''
    supermercados_facturacion = compras_por_supermercados(compras)
    ranking = sorted( supermercados_facturacion.items(), key = lambda tuplas:tuplas[1], reverse = True)[:n]
    return list(enumerate(ranking, 1))

def compras_por_supermercados(compras):
    supermercados_facturacion= {}
    for compra in compras:
        if compra.supermercado not in supermercados_facturacion:
            supermercados_facturacion[compra.supermercado] = compra.total_compra
        else:
            supermercados_facturacion[compra.supermercado] += compra.total_compra
    return supermercados_facturacion

#----------------------------------------------------------------------------------------------------------------------------

def clientes_itinerantes(compras, n):
    '''
    Devuelve una lista de tuplas con el dni del cliente y 
    la lista de provincias donde el cliente ha realizado sus compras,
    ordenadas alfabéticamente. Solo se devolverán 
    aquellos clientes que hayan comprado en un número de 
    provincias mayor que el parámetro n
    Entrada:
     - compras: lista de tuplas con la información de compras
         -> [[Compra(str,str,str,datetime,datetime,float)]
     - n: umbral de número de provincias -> int

    Salida:
     - lista de tuplas conteniendo 1) el dni del cliente y
       2) la lista con las provincias donde ha comprado -> [(str, [str])]
    '''
    clientes_itinerantes = {}
    clientes_provincias = provincias_por_cliente(compras)
    for dni, conjunto_provincias in clientes_provincias.items():
        if(len(conjunto_provincias) > n):
            clientes_itinerantes[dni] = sorted(conjunto_provincias)
    return list(clientes_itinerantes.items())

def provincias_por_cliente(compras):
    clientes_provincias = {}
    for compra in compras:
        if compra.dni not in clientes_provincias:
            provincias = set()
            provincias.add(compra.provincia)
            clientes_provincias[compra.dni] = provincias
        else:
            clientes_provincias[compra.dni].add(compra.provincia)
    return clientes_provincias

#----------------------------------------------------------------------------------------------------------------------------

def dias_estrella(compras, supermercado, provincia):
    '''
    Devuelve la lista ordenada de fechas estrella del supermercado 
    de una provincia. Se consideran estrella los días que facturan 
    más que el anterior y más que el siguiente. Recuerda que puedes 
    conseguir la fecha a partir de una fecha/hora fh con fh.date()
    Entrada:
     - compras: lista de tuplas con la información de compras
         -> [[Compra(str,str,str,datetime,datetime,float)]
     - supermercado: marca supermercado a analizar -> str
     - provincia: nombre provincia a analizar -> str

    Salida:
     - lista de fechas con los días estrellas ordenados -> [date]
    '''
    dias_facturacion = compras_por_fecha_salida(compras, supermercado, provincia)
    dias_ordenados = sorted(dias_facturacion.keys())
    dias_estrella= dias(dias_ordenados, dias_facturacion)
    return dias_estrella

#Función auxiliar: días facturados
def compras_por_fecha_salida(compras, supermercado, provincia):
    dias_facturacion = {}
    for compra in compras:
        if compra.supermercado == supermercado and compra.provincia == provincia: #filtro
            if compra.fecha_salida.date() in dias_facturacion:
                dias_facturacion[compra.fecha_salida.date()] += compra.total_compra
            else:
                dias_facturacion[compra.fecha_salida.date()] = compra.total_compra
    return dias_facturacion

#Función auxiliar para el cálculo de días, con range 
def dias(dias_ordenados, fact_por_dias):
    dias_estrella = list()
    for i in range(1, len(dias_ordenados) - 1):
        facturacion_ayer = fact_por_dias[dias_ordenados[i-1]]
        facturacion_hoy = fact_por_dias[dias_ordenados[i]]
        facturacion_mañana = fact_por_dias[dias_ordenados[i+1]]
        if facturacion_hoy > facturacion_ayer and facturacion_hoy > facturacion_mañana:
            dias_estrella.append(dias_ordenados[i])
    return dias_estrella
