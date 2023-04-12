import turtle
import time
import random


retraso = 0.1
marcador = 0
marcador_alto = 0


s = turtle.Screen()
s.setup(900, 900)
s.title("SNAKE")
s.bgcolor("black")



auxdesplazar = 23

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"
serpiente.color("lightgreen")


comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.speed(0)
comida.goto((random.randint(-400, 400)), random.randint(-400, 400))
comida.shapesize(0.5, 0.5, 0.5)

cuerpo = []
rgbcolor = ["red", "blue", "yellow", "white"]
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 415)
texto.write(f"Marcador: {marcador} \t  Marcador mas alto:  {marcador_alto}", align="center", font=("verdana", 24, "normal"))

def arriba():
    serpiente.direction = 'up'


def abajo():
    serpiente.direction = 'down'


def derecha():
    serpiente.direction = 'right'


def izquierda():
    serpiente.direction = 'left'


def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + auxdesplazar)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - auxdesplazar)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + auxdesplazar)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - auxdesplazar)



s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

s.onkeypress(arriba, "w")
s.onkeypress(abajo, "s")
s.onkeypress(derecha, "d")
s.onkeypress(izquierda, "a")


while True:
    s.update()

    if serpiente.xcor() > 450 or serpiente.xcor() < -450 or serpiente.ycor() > 450 or serpiente.ycor() < -450:
        time.sleep(1)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()
        texto.clear()
        marcador = 0
        texto.write(f"Marcador: {marcador} \t  Marcador mas alto:  {marcador_alto}", align="center",
                    font=("verdana", 24, "normal"))

    if serpiente.distance(comida) < 20:

        comida.goto((random.randint(-440, 440)), random.randint(-440, 440))

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("lightgreen")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0, 0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)
        marcador = marcador + 10
        texto.clear()
        texto.write(f"Marcador: {marcador} \t  Marcador mas alto:  {marcador_alto}", align="center",
                    font=("verdana", 24, "normal"))
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write(f"Marcador: {marcador} \t  Marcador mas alto:  {marcador_alto}", align="center", font=("verdana", 24, "normal"))

    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)
        cuerpo[index].shapesize(0.5, 0.5, 0.5)
        cuerpo[index].shapesize(0.7, 0.7, 0.7)
        cuerpo[index].color(random.choice(rgbcolor))
        cuerpo[index].color("lightgreen")


    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)





    movimiento()




    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"
            marcador = 0
            texto.clear()
            texto.write(f"Marcador: {marcador} \t  Marcador mas alto:  {marcador_alto}", align="center",
                        font=("verdana", 24, "normal"))
    time.sleep(retraso)









turtle.done()