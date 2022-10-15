'''
Created on 26 ene 2022

@author: macdemarco
'''
# IMPORTACIONES
import csv
from datetime import datetime
from collections import namedtuple, Counter


Compra = namedtuple('Compra', 'dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra')

# FUNCIONES

# EJERCICIO 1 

def lee_compras(fichero):
    lista_res = []
    
    with open(fichero, encoding = 'utf-8') as f:
        
        lector = csv.reader(f)
        next(lector)
        
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M')
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M')
            
            total_compra = float(total_compra)
            
            lista_res.append(Compra(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra))
            
        return lista_res


# EJERCICIO 2

def compra_maxima_minima_provincia(compra, provincia):
    compras = [e for e in compra if provincia == None or provincia == e.provincia]
    
    maximo = max(compras, key = lambda compras:compras.total_compra)
    
    minimo = min(compras, key = lambda compras:compras.total_compra)
    
    return (maximo.total_compra, minimo.total_compra)

# EJERCICO 3

def hora_menos_afluencia(compra):
    clientes_por_hora = Counter(e.fecha_llegada.hour for e in compra)
    
    return min(clientes_por_hora.items(), key = lambda x:x[1])

# EJERCICIO 4

def supermercados_mas_facturacion(compra, n):
    fact_por_sup = facturacion_por_supermercado(compra)
    ranking = sorted(fact_por_sup.items() ,key = lambda x:x[1], reverse = True)[:n]
    
    return list(enumerate(ranking, 1))

def facturacion_por_supermercado(compra):
    res = dict()
    for e in compra:
        if e.supermercado not in res:
            res[e.supermercado] = e.total_compra
        else:
            res[e.supermercado] += e.total_compra
    return res
    
# EJERCICIO 5
  
def clientes_itinerantes(compra, n):    
    cliente_prov = clientes_por_provincias(compra)
            
    res = {dni:sorted(conjunto_provincias) for dni, conjunto_provincias in cliente_prov.items() if (len(conjunto_provincias) > n)}
    
    return list(res.items())

def clientes_por_provincias(compra):
    cliente_prov = {}
    for e in compra:
        if e.dni not in cliente_prov:
            conj_prov = set()
            conj_prov.add(e.provincia)
            cliente_prov[e.dni] = conj_prov
        else: 
            cliente_prov[e.dni].add(e.provincia)
    
    return cliente_prov

# EJERCICIO 6
#dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra

def dias_estrella(compra, supermercado, provincia):
    
    factura_por_fecha = compra_fecha_salida(compra, supermercado, provincia)
    fecha_ordenada = sorted(factura_por_fecha.keys())
    dias_estrella = dias_estrellas(fecha_ordenada, factura_por_fecha)
    return dias_estrella

def compra_fecha_salida(compra, supermercado, provincia):
    res = dict()
    
    for e in compra:
        if e.supermercado == supermercado and e.provincia == provincia:
            if e.fecha_salida not in res:
                res[e.fecha_salida] = e.total_compra
            else:
                res[e.fecha_salida] += e.total_compra
        
    return res

def dias_estrellas(fecha_ordenada, factura_por_fecha):    
    
    dias_estrellas = list()
    
    for i in range(1, len(fecha_ordenada) - 1):
        ayer = factura_por_fecha[fecha_ordenada[i-1]]
        hoy = factura_por_fecha[fecha_ordenada[i]]
        mañana = factura_por_fecha[fecha_ordenada[i+1]]
        if hoy > ayer and hoy > mañana:
            dias_estrellas.append(fecha_ordenada[i])
    return dias_estrellas
    
    
    
    
    
    
    
    
    
    


