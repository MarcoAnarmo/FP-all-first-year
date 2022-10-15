'''
Created on 25 ene 2022

@author: macdemarco
'''

# Importaciones
import csv
from collections import namedtuple,Counter
from datetime import datetime

Gasto = namedtuple('Gastos', 'num_gasto,usuario,concepto,destinatario,cantidad,fecha')

# Funciones

# Ejercicio 1)

def lee_gastos(fichero):
    
    lista = []
    
    with open (fichero, encoding = 'utf-8') as f:
        
        lector = csv.reader(f)
        next(lector)
        
        for num_gasto,usuario,concepto,destinatario,cantidad,fecha in lector:
            num_gasto = int(num_gasto)
            cantidad = float(cantidad)
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            tupla = Gasto(num_gasto,usuario,concepto,destinatario,cantidad,fecha)
            lista.append(tupla)
            
        return lista
    

# Ejercicio 2)

def pagadores_y_conceptos(gasto):
    
    pagadores = sorted({e.usuario for e in gasto})
    
    conceptos = sorted({e.concepto for e in gasto})
    
    return pagadores, conceptos

# Ejercicio 3)

def total_importe(gasto, fecha_inicial = None, fecha_final = None):
    
    if fecha_inicial:
        fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y').date()
        
    if fecha_final:
        fecha_final = datetime.strptime(fecha_final, '%d/%m/%Y').date()

    return sum(e.cantidad for e in gasto if (fecha_inicial == None or fecha_inicial <= e.fecha) and (fecha_final == None or e.fecha <= fecha_final))

# Ejercicio 4)

def conceptos_menos_gastos(gasto):
    #num_gasto,usuario,concepto,destinatario,cantidad,fecha
    
    transacciones_conceptos = Counter(e.concepto for e in gasto)
    res = []
    minimo = min(transacciones_conceptos.values())
    
    for concepto, cuenta in transacciones_conceptos.items():
        if cuenta == minimo:
            res.append(concepto)
    return res
            
# Ejercicio 5)

def pagadores_mayor_importe_medio(gasto, n=3):
    
    total_por_usuario = dicc_aux(gasto)
    contador_por_usuario = Counter(e.usuario for e in gasto)
    medias = dict()
    for e in total_por_usuario:
        medias[e] = total_por_usuario[e]/contador_por_usuario[e]
    return sorted(medias.items(), reverse = True, key = lambda t:t[1])[:n]
    
def dicc_aux(gasto):
    
    res = dict()
    for e in gasto:
        if e.usuario not in res:
            res[e.usuario] = e.cantidad
        else:
            res[e.usuario] += e.cantidad
    return res
    









