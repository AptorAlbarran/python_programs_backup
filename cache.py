import numpy as np
num_elem = 10
indice = [*range(1, num_elem + 1)]
dato = np.random.normal(4, 3, num_elem)
dato[dato < 0] = 0 # esto se ocupa para evitar numeros negativos en "dato"
tamaño = 0.008 + 5 * np.random.rand(num_elem) # de 8kb a 5b
num_access = np.random.choice(num_elem, num_elem, replace=False)
for i in range(len(indice)):
   print(indice[i], dato[i], tamaño[i], num_access[i], sep="     ")

# memoria cache
import sys
L1=L2=L3=0
print('\n','estados de las memorias:\n','L1:',L1,'\n','L2:',L2,'\n','L3:',L3)
print('llenando memorias...\n')
L1=bytearray(127000)
L2=bytearray(999000)
L3=bytearray(49000000)
print('L1','1',sys.getsizeof(L1))
print('L2','2',sys.getsizeof(L2))
print('L3','3',sys.getsizeof(L3))
