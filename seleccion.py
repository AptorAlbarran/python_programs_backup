import numpy as np

def binADec(binario):
    dec = 0
    tam = len(binario)
    pot = 0
    j = tam-1
    for i in range(tam):
        dec+=np.power(2,pot)*binario[j]
        pot+=1
        j-=1
    return dec

def genAfenotipo(individuo):
    x=individuo[0:4]
    z=individuo[4:8]
    y=individuo[8:11]
    x=binADec(x)
    y=binADec(y)
    z=binADec(z)
    return(x,y,z)

def evalua(fem):
    x,y,z = fem
    if y>0:
        return (x*x+z*z)/(y*y)
    else:
        return 0

def funcionEvaluacion(codGen):
    fenotipo = genAfenotipo(codGen)
    return evalua(fenotipo)

def rankeo(poblacion):
    sumaTotal = 0
    evaluacion = []
    for individuo in poblacion:
        evaluacion.append(funcionEvaluacion(individuo))
        sumaTotal+=evaluacion[-1]
    porcentajes = []
    acumulado = [0]
    for desempenio in evaluacion:
        porcentajes.append(desempenio/sumaTotal)
        acumulado[-1]=acumulado[-1]+porcentajes[-1]
        acumulado.append(acumulado[-1])

    return acumulado

def seleccion(acumulado):
    r=np.random.rand()
    i=0
    while(r>acumulado[i]):
        i+=1
    a= i-1
    r=np.random.rand()
    i=0
    while(r>acumulado[i]):
        i+=1
    return a,i-1
