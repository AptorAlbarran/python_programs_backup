from graphics import *
import numpy as np

win = GraphWin("laberinto", 600, 600)
n = 20
laberinto = np.random.normal(0.5, 0.3,(n,n))
h = win.getHeight()/n
w = win.getWidth()/n
for i in range(n):
    for j in range(n):
        rect = Rectangle(Point(w*i, h*j), Point(w*i+w, h*i+h))
        if(not laberinto[i,j] < 0.1 or laberinto[i,j] > 0.9):
            rect.setFill("black")
        else:
            rect.setFill("white")
        rect.draw(win)

win.getMouse()
win.close()
