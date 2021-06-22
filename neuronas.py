import numpy as np

class neurona:
	pesos = []
	sesgo = 0
	salida = 0

	def __init__(self,P,s):
		self.pesos = P
		self.sesgo = s

	def __init__(self,n):
		self.pesos = np.random.random(n)
		self.sesgo = np.random.rand()

	def procesaSalida(self,entrada):
		suma = 0
		n = len(self.pesos)
		for i in range(n):
			suma+=entrada[i]*self.pesos[i]
		self.salida = self.funcionActivacion(suma+self.sesgo)

	def funcionActivacion(self,x):
		return 1/(1+np.exp(-x))

#A = neurona(6)
#A.procesaSalida([0,1,2,3,4,5])
#print('pesos:',A.pesos)
#print('sesgo:',A.sesgo)
#print('salidas:',A.salida)

#B = neurona(5)
#B.procesaSalida([0,1,2,3,4])
#print('pesos:',B.pesos)
#print('sesgo:',B.sesgo)
#print('salidas:',B.salida)

# en el futuro donde se quiera hacer otra neurona desde la terminal
# tener el cuenta que se necesita hacer - import neurona from neurona -
# ya que la clase se llama igual que el archivo por lo que al querer
# hacer uso de "neurona" va a pensar que nos estamos refierendo al
# archivo y tirara un error, hacer esto en los demas archivos o
# cambiar el nombre del mismos

# update: cambie el nombre a 'neuronas'

class red:
	A=[]
	B=[]
	salida=[]

	def __init__(self,n,nA,nB):
		for i in range(nA):
			self.A.append(neurona(n))
		for i in range(nB):
			self.B.append(neurona(nA))

	def procesaSalida(self,entrada):
		salidaA=[]
		for i in range(len(self.A)):
			self.A[i].procesaSalida(entrada)
			salidaA.append(self.A[i].salida)

		for i in range(len(self.B)):
			self.B[i].procesaSalida(salidaA)
			self.salida.append(self.B[i].salida)

R=red(4,5,3)
