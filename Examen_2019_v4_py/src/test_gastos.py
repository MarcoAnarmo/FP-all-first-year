'''
Created on 25 ene 2022

@author: macdemarco
'''
#importaciones

from gastos import *

#funciones

def test_lee_gastos():
    
    lista_tuplas= lee_gastos('../data/gastos.csv')
    
    print(lista_tuplas[:3])

def test_pagadores_y_conceptos():
    print('\n------------------------------------------------------------------------\n')
    lista_tuplas= lee_gastos('../data/gastos.csv')
    
    pagadores, conceptos = pagadores_y_conceptos(lista_tuplas)
    print('Pagadores: ', pagadores)
    print('Conceptos: ', conceptos)

def test_total_importe():
    print('\n------------------------------------------------------------------------\n')
    lista_tuplas= lee_gastos('../data/gastos.csv')
    
    print("La cantidad total gastada:", total_importe(lista_tuplas))
    print('La cantidad total gastada entre el 5 y el 8 de abril de 2019 fue:', total_importe(lista_tuplas, '05/04/2019', '08/04/2019'))
    
def test_conceptos_menos_gastos():
    print('\n------------------------------------------------------------------------\n')
    lista_tuplas= lee_gastos('../data/gastos.csv')
    
    print('Los conceptos con menos gastos registrados son:', conceptos_menos_gastos(lista_tuplas))


def test_pagadores_mayor_importe_medio():
    print('\n------------------------------------------------------------------------\n')
    lista_tuplas= lee_gastos('../data/gastos.csv')
    
    print('Los tres pagadores con un mayor importe medio en sus gastos son:\n', pagadores_mayor_importe_medio(lista_tuplas))




#main

if __name__ == '__main__':
    test_lee_gastos()
    test_pagadores_y_conceptos()
    test_total_importe()
    test_conceptos_menos_gastos()
    test_pagadores_mayor_importe_medio()