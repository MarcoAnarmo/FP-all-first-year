# -*- encoding utf-8 -*-

'''
Created on 24 ene 2022

@author: macdemarco
'''

from concesionarios import *

def test_lee_ventas():

    resultado = lee_ventas("../data/concesionarios.csv")

    print("Las tres primeras son: ", resultado[:3])
        
    print("Las tres últimas son: ", resultado[-3:])
    
    
def test_unidades_vendidas():
    lista_tuplas = lee_ventas("../data/concesionarios.csv")
    
    resultado,modelos, fecha_inicial, fecha_final = unidades_vendidas(lista_tuplas, ('MODELO-A', 'MODELO-C'), '1/1/2017', '1/3/2017')
    
    print("El número de unidades vendidas de los modelos ", modelos, "entre el", fecha_inicial, "y el", fecha_final, "es:", resultado)
    
def test_dicc_beneficios_por_modelo_año():
    lista_tuplas = lee_ventas("../data/concesionarios.csv")
    
    resultado, año = dicc_beneficios_por_modelo_año(lista_tuplas, 2016)
    
    print("El beneficio por modelo en el año", año, "es:", resultado)
    
def test_dias_de_mas_unidades():
    lista_tuplas = lee_ventas("../data/concesionarios.csv")
    
    print("Las fechas de las ventas con más unidades vendidas fueron 2 y son:", dias_de_mas_unidades(lista_tuplas))
    
def test_lista_dif_unidades_mes():
    lista_tuplas = lee_ventas("../data/concesionarios.csv")
    
    print('La lista de diferencia de ventas por mes es:', lista_dif_unidades_mes(lista_tuplas))

def test_modelos_vendidos_mas_n_en_año():
    lista_tuplas = lee_ventas("../data/concesionarios.csv")
    
    print(modelos_vendidos_mas_n_en_año(lista_tuplas, 2012, 2))
    
if __name__ == '__main__':
    test_lee_ventas()
    test_unidades_vendidas()
    test_dicc_beneficios_por_modelo_año()
    test_dias_de_mas_unidades()
    test_lista_dif_unidades_mes()
    test_modelos_vendidos_mas_n_en_año()
