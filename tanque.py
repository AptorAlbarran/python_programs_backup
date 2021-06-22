import math
#ht=2.43 # altura del tanque
ht=float(input("dame la altura del tanque en metros: ")) # str a float
#v0=1375 # velocidad inicial a la que se dispara la bala
v0=float(input("dame la velocidad a la que saldrá la bala: "))
#angulo1=60 # angulo de inclinacion de disparo de arriba a abajo
angulo1=float(input("dame el angulo de disparo: "))
#ho=0 # altura del objetivo (se esta pensando en que se dispara al suelo)
ho=float(input("dame la altura del objetivo en metros: "))
#print(ht,v0,angulo1,ho)
a=-4.9 # gravedad/2
b=v0*math.sin(math.radians(angulo1)) # de rad a deg
c=ht
d=(b**2)-(4*a*c)
t1=(-b-math.sqrt(d))/(2*a)
x=ho+(v0*math.cos(math.radians(angulo1)))*t1
print('la bala caerá a {0} metros'.format(x))
