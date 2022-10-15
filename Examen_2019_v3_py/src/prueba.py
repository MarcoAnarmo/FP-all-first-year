'''
Created on 24 ene 2022

@author: macdemarco
'''
from datetime import datetime


if __name__ == '__main__':
    
    fecha_hora = "13/04/2017 17:04"
    
    fecha_hora = datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M")
    
    print(fecha_hora)