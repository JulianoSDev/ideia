import math
import time
from turtle import *


def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


speed(0)
bgcolor("black")
penup()  
goto(0, 0)
pendown() 

color("red")  
pensize(2)


for i in range(0, 360, 1):  
    x = hearta(i * math.pi / 180) * 20  
    y = heartb(i * math.pi / 180) * 20  
    goto(x, y)
    update() 
penup()
goto(0, -100)
color("white")
pendown()

for i in range(10):  
    write("I love U", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)  
time.sleep(3)

done()
