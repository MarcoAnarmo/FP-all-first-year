# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:51:21 2020

@author: Damián Fernández
@revisor: Pepe Riquelme, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

from compras import *

def test_lee_compras(compras):
    print("Número de registros leídos:", len(compras))
    print("Tres primeros registros:", compras[:3])
    print("Tres últimos registros:", compras[-2:])
    
def test_compra_maxima_minima_provincia(compras):
    provincia = "Huelva"
    importes = compra_maxima_minima_provincia(compras, "Huelva") 
    print("Importe máximo de la provincia de", provincia, ":", importes[0],
        "Importe mínimo:", importes[1])

def test_hora_menos_afluencia(compras):
    horas = hora_menos_afluencia(compras)
    print("La hora con menos afluencia es:", horas[0], "h. con", horas[1],
          "llegadas de clientes")

def test_supermercados_mas_facturacion(compras):
    n = 2
    supermercados = supermercados_mas_facturacion(compras, n)
    print("Los", n, "Supermercados con más facturación son:", supermercados)
                                                                
def test_clientes_itinerantes(compras):
    n=7
    clientes_itinerates = clientes_itinerantes(compras, n)
    print("Los clientes itinerantes que han comprado al menos en n", n, "provincias son:", 
        clientes_itinerates)
        
def test_dias_estrella(compras):
    supermercado = "Aldi"
    provincia = "Huelva"
    dias = dias_estrella(compras, supermercado, provincia)
    print("Los días estrella del supermercado", supermercado, "de la provincia de",
          provincia, "son:", [dia_estrella.strftime('%d/%m/%Y') for dia_estrella in dias])
                                                                 
    
if __name__=="__main__":
    print("\nEJERCICIO 1")
    
    compras = lee_compras("../data/compras.csv")
    
    test_lee_compras(compras)

    print("\nEJERCICIO 2")
    test_compra_maxima_minima_provincia(compras)
    print("\nEJERCICIO 3")
    test_hora_menos_afluencia(compras)
    print("\nEJERCICIO 4")
    test_supermercados_mas_facturacion(compras)
    print("\nEJERCICIO 5")
    test_clientes_itinerantes(compras)
    print("\nEJERCICIO 6")
    test_dias_estrella(compras)
