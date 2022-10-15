'''
Created on 26 ene 2022

@author: macdemarco
'''
# IMPORTACIONES

from compras import *

# FUNCIONES 

def test_lee_compras(compras):
    print('EJERCICIO 1:\n')
    
    print("Número de registros leidos:", len(compras))
    print('\nTres primeros registros:', compras[:3])
    print('\nTres últimos registros:', compras[-3:])

def test_compra_maxima_minima_provincia(compras):
    print('\n----------------------------------------------------------------\n')
    print('EJERCICIO 2:\n')
    
    provincia = 'Huelva'
    res = compra_maxima_minima_provincia(compras, provincia)
    
    print('Importe máximo de la provincia de', provincia, ':', res[0], '. Importe mínimo:', res[1])
    
def test_hora_menos_afluencia(compras):
    print('\n----------------------------------------------------------------\n')
    print('EJERCICIO 3:\n')

    res = hora_menos_afluencia(compras)
    
    print(f'La hora con menos afluencia es: {res[0]}h. Con {res[1]} llegadas de clientes.')

def test_supermercados_mas_facturacion(compras):
    print('\n----------------------------------------------------------------\n')
    print('EJERCICIO 4:\n')
    
    n = 2
    res = supermercados_mas_facturacion(compras, n)
    print(f'Los {n} supermercados con más facturación son: {res}')

def test_clientes_itinerantes(compras):
    print('\n----------------------------------------------------------------\n')
    print('EJERCICIO 5:\n')
    
    n = 7
    res = clientes_itinerantes(compras, n)
    print(f'Los clientes itinerantes que han comprado al menos en {n} provincias son:', res)

def test_dias_estrella(compras):
    print('\n----------------------------------------------------------------\n')
    print('EJERCICIO 6:\n')
    
    supermercado = "Aldi"
    provincia = "Huelva"
    dias = dias_estrella(compras, supermercado, provincia)
    print("Los días estrella del supermercado", supermercado,'la provincia de', provincia, "son:", [dia_estrella.strftime('%d/%m/%Y')for dia_estrella in dias])
                                                                                  
                                                                                  
                                                                                  
# MAIN

if __name__ == '__main__':
    
    compras = lee_compras('../data/compras.csv')
    
    test_lee_compras(compras)
    test_compra_maxima_minima_provincia(compras)
    test_hora_menos_afluencia(compras)
    test_supermercados_mas_facturacion(compras)
    test_clientes_itinerantes(compras)
    test_dias_estrella(compras)
    
    
    
    
    
    
    
    
    
    
    
    
    
    