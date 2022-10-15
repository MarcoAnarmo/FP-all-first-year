'''
Created on 5 oct 2021

@author: macdemarco
'''
from pip._vendor.distlib.compat import raw_input

def calcula_nota_cuestionario (n1, n2, n3):
    
    nota = ((n1 * 10)/(n3)) - ((n2 * 10)/(50 - n3)) 
    
    print("------------------------------")
    
    if nota == 10:
        print("Enhorabuena!! A celebrarlo que tienes un 10.")
        
    elif nota < 0:
        print("Has sacado nota negativa, a ver si estudiamos más.")
    
    elif nota > 10:
        print("Te has debido equivocar con el número total de respuestas, tu nota es:", nota)
        
    elif nota < 5:
        print("La próxima será, hay que estudiar un poco más, tienes un:", nota)
        
    elif nota >= 5:
        print("Enhorabuena, has aprobado, tienes un:", nota)
    
    return (nota)


def lee_datos_cuestionario ():
    
    print("")
    print("#### NOTA CUESTIONARIO ####")
    print("")
    
    x = int(input("Número de respuestas correctas: "))
    
    if x < 0:
        return(print("Error, No se admite una respuesta negativa"))
        
    y = int(input("Número de errores que has tenido: "))
    
    if y < 0:
        return(print("Error, No se admite una respuesta negativa"))
        
    z = int(input("Número total de respuestas: "))
    
    if z < 0:
        return(print("Error, No se admite una respuesta negativa"))
    
    return(x, y, z)


def main_nota_cuestionario():
    
    aciertos, errores, totalRespuestas = lee_datos_cuestionario()
    
    calcula_nota_cuestionario(aciertos, errores, totalRespuestas)
    
    
def calcula_nota_cuatrimestre ():
    print("")
    print("#### NOTA CUATRIMESTRE ####")
    print("")
    
    c = []
    c.append(float(raw_input("Nota del primer cuestionario: ")))
    c.append(float(raw_input("Nota del segundo cuestionario: ")))
    c.append(float(raw_input("Nota del tercer cuestionario: ")))
    
    def nota_del_parcial():
        parcial = float(raw_input("Nota del parcial: "))
        return(parcial)
    
    parcial = nota_del_parcial()
    pry = float(raw_input("Nota del proyecto: "))
    
    print("------------------------------")
    
    if pry < 5.0:
        nota_cuatrimestre = 3
        print("Tu nota del cuatrimestre es", nota_cuatrimestre, "porque has suspendido el proyecto." )
        
    else:
        
        nota_cuatrimestre= (0.13 * (c[0]+ c[1] + c[2]) + (0.5 * parcial) + (0.1 * pry))
        print("Tu nota del cuatrimestre es: ", nota_cuatrimestre)
        
    return(nota_cuatrimestre, parcial)


def calcula_nota_evaluacion_continua (nc1, nc2):
    
    print("")
    print("#### NOTA DE LA EVALUACIÓN CONTINUA ####")
    print("")
    
    nota_ev_continua = (nc1 + nc2)/2
    
    print("Tu nota de la evaluación continua es:", nota_ev_continua)
    
    return(nota_ev_continua)


def main_calcula_nota_evaluacion_continua():
    nota_cuatrimestre1 = calcula_nota_cuatrimestre()
    nota_cuatrimestre2 = calcula_nota_cuatrimestre()
    
    if nota_cuatrimestre1 != float():
        print("Has suspendido el primer cuatrimestre y se hace media con un 3")
        nota_cuatrimestre1 = 3
        
    elif nota_cuatrimestre2 != float():
        print("Has suspendido el segundo cuatrimestre y se hace media con un 3")
        nota_cuatrimestre2 = 3
        
    calcula_nota_evaluacion_continua(nota_cuatrimestre1, nota_cuatrimestre2)

