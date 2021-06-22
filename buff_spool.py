import numpy as np
num_elem = 5 # este programa se probo con 10 elementos y aun asi se tardaba algo
N = [*range(1, num_elem + 1)]
tamaño = np.random.normal(156, 46, num_elem) # 156 = media, 46 = desviacion
prioridad = 1 + 5 * np.random.rand(num_elem) # array de numeros random de 1 a 5
def bogosort(x): # esto sirve par ordenar prioridad
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x
bogosort(prioridad)
#print("N#")
#print(N)
#print("tamaño")
#print(tamaño)
#print("prioridad")
#print(x)
for i in range(len(N)):
    print (N[i], tamaño[i], prioridad[i], sep="     ")
