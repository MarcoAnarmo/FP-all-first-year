'''
Created on 16 nov 2021

@author: macdemarco
'''

import csv
from collections import namedtuple, Counter
from matplotlib import pyplot as plt

Pregunta = namedtuple("Pregunta" , "puntuacion, titulo, año, etiqueta")

def leer_preguntas(fichero):
    
    with open (fichero, encoding = "utf-8") as f:
        
        lector = csv.reader(f)
        
        next(lector)
        
        preguntas = [Pregunta (int(puntuacion), titulo, int(año), etiqueta)
                             for puntuacion, titulo, año, etiqueta in lector]
        
        return preguntas



def filtrar_por_año(preguntas, año):

    return [p for p in preguntas if p.año == año]



def calcular_etiquetas(preguntas):
    
    etiquetas = [p.etiqueta for p in preguntas]
    
    return etiquetas

def calcular_preguntas_mejor_valoradas(preguntas, limite=10):
    
    mejor_valoradas = [(p.titulo, p.puntuacion) for p in preguntas]
    
    mejor_valoradas.sort(key=lambda x:x[1], reverse=True)
    
    return mejor_valoradas[:limite]

def contar_etiquetas(preguntas):
    
    etiquetas = [p.etiqueta for p in preguntas]
    
    frecuencias = Counter(etiquetas)
    
    return dict(frecuencias)

def mostrar_distribucion_de_etiquetas(preguntas,etiquetas):
    
    frecuencias = contar_etiquetas(preguntas)
    tamaños = [frecuencias.get(e,0) for e in etiquetas]
    plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.legend()
    plt.show()
    pass

def calcular_palabras_claves(titulo, stopwords=[]):
    
    
    return 

