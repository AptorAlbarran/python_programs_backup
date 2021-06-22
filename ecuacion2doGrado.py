# resolver ecuacion cuadratica de 2do grado
# ax**2+bx+c=0
# se ocupara la chicharronera (la formula general)
import cmath
a=1
b=5
c=6
d=(b**2)-(4*a*c) # aqui se pone lo que ira dentro de la raiz cuadrada
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('la solucion es {0} y {1}'.format(sol1,sol2))
