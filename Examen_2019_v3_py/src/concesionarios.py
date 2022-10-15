# -*- encoding utf-8 -*-

'''
Created on 24 ene 2022

@author: macdemarco
'''
# Importaciones
import csv
from collections import namedtuple, Counter
from datetime import datetime

Venta = namedtuple('Ventas', 'fecha,ciudad,modelo,precio,unidades,financiado')

# Funciones

# Ejercicio 1)
def lee_ventas(fichero):
    '''
    Input: fichero csv de tipo ventas
    Output: lista de tuplas del tipo ventas
    '''
    lista = [] 
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        
        for fecha,ciudad,modelo,precio,unidades,financiado in lector:
            
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            precio = float(precio)
            unidades = int(unidades)
            if financiado == 'SI':
                financiado = True
            else:
                financiado = False
            
            tupla = Venta(fecha,ciudad,modelo,precio,unidades,financiado)
            lista.append(tupla)
            
    return lista

# Ejercicio 2)
def unidades_vendidas(ventas, modelos, fecha_inicial = None, fecha_final = None):
    '''
    Input: lista de tuplas del tipo ventas, conjunto de modelos, fecha inicial, fecha final.
    Output: total de unidades vendidas de los modelos de automóvil que figuran en el conjunto entre las dos fechas, ambas incluidas.
    '''
    #fecha,ciudad,modelo,precio,unidades,financiado
    
    fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y').date()
    fecha_final = datetime.strptime(fecha_final, '%d/%m/%Y').date()
    
    res= sum([e.unidades for e in ventas if (e.modelo in modelos) and (fecha_inicial<= e.fecha <=fecha_final)])
    
    return res, modelos, fecha_inicial, fecha_final

# Ejercicio 3)
def dicc_beneficios_por_modelo_año(ventas, año):
    '''
    Input: lista de tuplas del tipo ventas y un año.
    Output: diccionario del tipo {modelo:beneficio} con el beneficio de ese modelo en el año especificado.
    '''
    #fecha,ciudad,modelo,precio,unidades,financiado
    res = dict()
    for venta in ventas:
        if venta.fecha.year == año:
            if venta.modelo not in res:
                res[venta.modelo] = beneficio(venta)
            else:
                res[venta.modelo] += beneficio(venta)
    return res, año

def beneficio(ventas):

    if ventas.financiado:
        beneficio = ventas.unidades * ventas.precio * 0.15
    else:
        beneficio = ventas.unidades * ventas.precio * 0.1
    return beneficio

# Ejercicio 4)
def dias_de_mas_unidades(ventas):
    '''
    Input: lista de tuplas del tipo ventas.
    Output: lista con los días en los que se realizó la venta con mayor número de unidades.
    '''
    #fecha,ciudad,modelo,precio,unidades,financiado
    
    max_ventas = max(ventas, key = lambda x: x.unidades)
    
    return [e.fecha for e in ventas if e.unidades == max_ventas.unidades]
    

# Ejercicio 5)
def lista_dif_unidades_mes(ventas):
    '''
    Input: lista de tuplas del tipo ventas.
    Output: lista con las diferencias del número de unidades vendidas acumuladas para todos los años de un mes con respecto al anterior.
    '''
    #fecha,ciudad,modelo,precio,unidades,financiado
    
    res = []
    for i in range(1,12):
        diferencia = unidades_vendidas_por_mes(ventas, i+1) - unidades_vendidas_por_mes(ventas, i)
        res.append(diferencia)
    return res
    

def unidades_vendidas_por_mes(ventas, mes):
    return sum([e.unidades for e in ventas if mes == e.fecha.month])
    
# Ejercicio 6)

def modelos_vendidos_mas_n_en_año(ventas, año, n):
    '''
    Input: lista de tuplas de tipo Venta, un año y un número n.
    Output: conjunto con los modelos que se han vendido durante ese año en más de n ciudades.
    ''' 
    #fecha,ciudad,modelo,precio,unidades,financiado
    
    dicc = agrupar_por_modelo(ventas,año)
    conjunto_modelos = set()
    for modelo, ciudades in dicc.items():
        if len(ciudades) > n:
            conjunto_modelos.add(modelo)
    return conjunto_modelos
    
    
def agrupar_por_modelo(ventas, año):
    dicc = {}
    for e in ventas:
        if e.fecha.year == año:
            if e.modelo not in dicc:
                dicc[e.modelo] = {e.ciudad}
            else:
                dicc[e.modelo].add(e.ciudad)
    return dicc













