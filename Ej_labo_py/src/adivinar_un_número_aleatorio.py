'''
Created on 19 oct 2021

@author: macdemarco
'''
import random

#GENERAR UN NÚMERO RANDOM

máximo = int(input("Introduce el valor máximo del número random: "))

objetivo = random.randint(1, máximo)


#LEER NÚMERO DE TECLADO

n = int(input("Introduce un número n: "))

print("El número introducido es: ", n)

#COMPROBAR SI COINCIDE n CON objetivo

if n == objetivo:
    
    print("Enhorabuena has acertado")
    
else:
    
    print("Lo siento has fallado, el número era", objetivo)


    