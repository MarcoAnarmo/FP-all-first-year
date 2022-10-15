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

#COMPROBAR SI COINCIDE n CON objetivo

while n != objetivo:
    
    if n < objetivo:
        
        print(f"Tu número {n} es menor al objetivo")
        
    elif n > objetivo:
        
        print(f"Tu número {n} es mayor al objetivo")
    
    n = int(input("Introduce un nuevo número: "))

print(f"Enhorabuena has acertado!! El número era {n}")