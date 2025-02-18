import math
import time
from turtle import *

# Funções do coração
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Configurações iniciais
speed(0)
bgcolor("black")
penup()  # Levanta a caneta para não desenhar enquanto move para a posição inicial
goto(0, 0)
pendown()  # Começa a desenhar

color("red")  # Cor única para o coração
pensize(2)

# Função para desenhar o coração com a cor única
for i in range(0, 360, 1):  # Definindo um intervalo adequado
    x = hearta(i * math.pi / 180) * 20  # Multiplicando por 20 para ajustar o tamanho
    y = heartb(i * math.pi / 180) * 20  # Multiplicando por 20 para ajustar o tamanho
    goto(x, y)
    update()  # Atualiza a tela para gerar a animação

# Exibindo a mensagem "I love U" após o desenho do coração
penup()
goto(0, -100)
color("white")
pendown()

# Mensagem aparecendo lentamente
for i in range(10):  # Para manter a mensagem por mais tempo
    write("I love U", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)  # Atraso maior para cada iteração (1 segundo)

# Mantendo a mensagem na tela por mais tempo
time.sleep(3)

done()
