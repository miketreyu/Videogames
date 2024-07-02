import turtle
#import tkinter as TK

#Window
window = turtle.Screen()
window.title("Pong by Mike")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Score
scoreA = 0
scoreB = 0

#PlayerA
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape('square')
playerA.color('white')
playerA.penup()
playerA.goto(-350,0)
playerA.shapesize(stretch_wid = 5, stretch_len = 1)

#PlayerB
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape('square')
playerB.color('white')
playerB.penup()
playerB.goto(350,0)
playerB.shapesize(stretch_wid = 5, stretch_len = 1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Line
line = turtle.Turtle()
line.color('white')
line.goto(0,400)
line.goto(0,-400)
#line.shapesize(stretch_wid = 5, stretch_len = 1)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('PlayerA: 0           PlayerB: 0', align = 'center', font = ('Courier', 24, 'normal'))

#Functions
def playerA_up():
    y = playerA.ycor()
    y += 20
    playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    y -= 20
    playerA.sety(y)

def playerB_up():
    y = playerB.ycor()
    y += 20
    playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    y -= 20
    playerB.sety(y)

def playerA_up():
    y = playerA.ycor()
    if y < 250:  
        y += 20
        playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    if y > -250:  
        y -= 20
        playerA.sety(y)

def playerB_up():
    y = playerB.ycor()
    if y < 250:  
        y += 20
        playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    if y > -250:  
        y -= 20
        playerB.sety(y)

#Keyboard
window.listen()
window.onkeypress(playerA_up, 'w')
window.onkeypress(playerA_down, 's')
window.onkeypress(playerB_up, 'Up')
window.onkeypress(playerB_down, 'Down')

while True:
    window.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Borders
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1
    
    #Left and right borders
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write('PlayerA: {}           PlayerB: {}'.format(scoreA, scoreB), align = 'center', font = ('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write('PlayerA: {}           PlayerB: {}'.format(scoreA, scoreB), align = 'center', font = ('Courier', 24, 'normal'))

    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < playerB.ycor() + 50
            and ball.ycor() > playerB.ycor() - 50)):
        ball.dx *= -1
    
    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < playerA.ycor() + 50
            and ball.ycor() > playerA.ycor() - 50)):
        ball.dx *= -1

'''
# Define una variable para controlar si el juego está pausado o no
is_game_paused = False

# Función para pausar y reanudar el juego
def pause_game():
    global is_game_paused
    if is_game_paused:
        window.update()  # Reanuda la actualización de la ventana
        is_game_paused = False
    else:
        is_game_paused = True

# Configurar el evento de teclado para pausar y reanudar el juego
window.onkeypress(pause_game, 'Esc')

# Bucle principal del juego
while True:
    if not is_game_paused:
        window.update()
        
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Resto del código del bucle principal del juego
        # (Movimiento de jugadores, colisiones, actualización de puntuación, etc.)







       
 # Variables para registrar el estado de las teclas
is_playerA_up_pressed = False
is_playerA_down_pressed = False
is_playerB_up_pressed = False
is_playerB_down_pressed = False

# Funciones de control de movimiento de los jugadores
def playerA_up():
    global is_playerA_up_pressed
    is_playerA_up_pressed = True

def playerA_down():
    global is_playerA_down_pressed
    is_playerA_down_pressed = True

def playerB_up():
    global is_playerB_up_pressed
    is_playerB_up_pressed = True

def playerB_down():
    global is_playerB_down_pressed
    is_playerB_down_pressed = True

# Función para mover a los jugadores basados en el estado de las teclas presionadas
def move_players():
    if is_playerA_up_pressed:
        y = playerA.ycor()
        if y < 250:
            y += 20
            playerA.sety(y)
    if is_playerA_down_pressed:
        y = playerA.ycor()
        if y > -250:
            y -= 20
            playerA.sety(y)
    if is_playerB_up_pressed:
        y = playerB.ycor()
        if y < 250:
            y += 20
            playerB.sety(y)
    if is_playerB_down_pressed:
        y = playerB.ycor()
        if y > -250:
            y -= 20
            playerB.sety(y)

# Configurar eventos de teclado
window.listen()
window.onkeypress(playerA_up, 'w')
window.onkeypress(playerA_down, 's')
window.onkeypress(playerB_up, 'Up')
window.onkeypress(playerB_down, 'Down')

# Bucle principal del juego
while True:
    window.update()
    move_players()
'''