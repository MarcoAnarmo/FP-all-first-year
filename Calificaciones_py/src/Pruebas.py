'''
Created on 12 oct 2021

@author: macdemarco
'''
from pip._vendor.distlib.compat import raw_input
def calcula_nota_cuatrimestre ():
    print("")
    print("#### NOTA CUATRIMESTRE ####")
    print("")
    
    c = []
    c.append(float(raw_input("Nota del primer cuestionario: ")))
    c.append(float(raw_input("Nota del segundo cuestionario: ")))
    c.append(float(raw_input("Nota del tercer cuestionario: ")))

    parcial = float(raw_input("Nota del parcial: "))
    
    pry = float(raw_input("Nota del proyecto: "))
    
    print("------------------------------")
    
    if pry < 5.0:
        nota_cuatrimestre = 3
        print("Tu nota del cuatrimestre es", nota_cuatrimestre, "porque has suspendido el proyecto." )
        
    else:
        
        nota_cuatrimestre= (0.13 * (c[0]+ c[1] + c[2]) + (0.5 * parcial) + (0.1 * pry))
        print("Tu nota del cuatrimestre es: ", nota_cuatrimestre)
        
    return(nota_cuatrimestre)

calcula_nota_cuatrimestre()