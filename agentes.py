import numpy as np

def cruza(A,B):
    puntoCruza = np.random.randint(0,len(A))
    descendiente1 = A[:puntoCruza] + B[puntoCruza:]
    descendiente2 = B[:puntoCruza] + A[puntoCruza:]
    return descendiente1, descendiente2

def mutacion(A):
    B=[]
    for gen in A:
        B.append(gen)
    puntoMutacion = np.random.randint(0,len(A))
    B[puntoMutacion] = A[puntoMutacion]*-1+1
    return B
