import pygame, sys, os
from pygame.locals import *

# Game Initialization
# El programa se inicializa aquí
pygame.init()

# Center the Game Application
# centramos el juego de la aplicación
os.environ['SDL_VIDEO_CENTERED']='1'

# Game Resolution
# Resolución del juego
screen_width=800 #anchura
screen_height=600 #altura
screen=pygame.display.set_mode((screen_width, screen_height)) #aquí colocamos la anchura y la altura de nuestro juego 

# Color
black=(0, 0, 0) # rgb red green blue 
white=(255, 255, 255)
blue=(0, 0, 255)

# Framerate #velocidad del fotograma 
clock=pygame.time.Clock() # llamando al reloj del juego
fps=200

# Initial Variables
lineWidth=10 #anchura linea 
paddleSize=50  #tamaño raqueta 
paddleOffset=20 #compensación de la raqueta


def BackgroundGameplay(): #fondo del juego 
    screen.fill(black) #llenar la pantalla de negro
    pygame.draw.line(screen, white, ((screen_width / 2), 0), ((screen_width / 2), screen_height), 2) #dibujar dos lineas blancas de un 
																									 #tamaño según una anchura y una altura
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth) #dibujar un rectángulo en la pantalla según un color,
																					   #una posición, una dimensión y unos tamaños dados.

def Paddle(paddle):
    pygame.draw.rect(screen, white, paddle)  #dibujamos la raqueta en la pantalla según un color y la forma de la raqueta

def Ball(ball):
    pygame.draw.rect(screen, white, ball) #dibujamos la bola en la pantalla según un color y la forma de la bola

def BallMovement(ball, ballDirX, ballDirY): #movimiento de la bola según unas coordenadas 
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

def main(): # programa que se ejecutará en primer lugar 

	# Vamos a conseguir las coordenadas de la bola
    ballPosX=screen_width/2 - lineWidth/2
    ballPosY=screen_height/2 - lineWidth/2

	# Posición de los jugadores
    playerPos=(screen_height-paddleSize)/2
    enemyPos=(screen_height-paddleSize)/2
    # Puntuación
    score=0
	
	#Coordenadas de la dirección de la bola
    ballDirX = -1
    ballDirY = -1

	# Aquí definimos la raqueta1, raqueta2 y la bola
    paddle1 = pygame.Rect(paddleOffset, playerPos, lineWidth, paddleSize)
    paddle2 = pygame.Rect(screen_width - paddleOffset - lineWidth, enemyPos, lineWidth, paddleSize)
    ball=pygame.Rect(ballPosX, ballPosY, lineWidth, lineWidth)

	#Llamamos a las funciones anteriormente definidas 
    BackgroundGameplay()
    Paddle(paddle1)
    Paddle(paddle2)
    Ball(ball)
    # Ponemos el puntero del ratón en invisible
    pygame.mouse.set_visible(1)
    
    #Mientras sea verdadero
    while True:
		#Recorremos el evento 
        for event in pygame.event.get():
			#Si se cumple tipo de evento, donde es igual a QUIT
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #Sino, se cumplirá el tipo de evento, donde es igual a MOUSEMOTION
            elif event.type==MOUSEMOTION:
                mousex, mousey=event.pos
                paddle1 = pygame.Rect(paddleOffset, mousey, lineWidth, paddleSize)
                print("Ratón: (x,y)=(", mousex, ", ", mousey)                
                
		#Llamamos a las funciones anteriormente definidas
        BackgroundGameplay()
        Paddle(paddle1)
        Paddle(paddle2)
        Ball(ball)

        if ball.x <= 0:
            ballDirX = +1
            ball=BallMovement(ball, ballDirX, ballDirY)
        if ball.x + lineWidth >= screen_width:
            ballDirX = -1
            ball=BallMovement(ball, ballDirX, ballDirY)
        if ball.y <= 0:
            ballDirY = +1
            ball=BallMovement(ball, ballDirX, ballDirY)
        if ball.y + lineWidth >= screen_height:
            ballDirY = -1
            ball=BallMovement(ball, ballDirX, ballDirY)
        else: 
            #Llamamos a la función de mover bola anteriormente definida
            ball=BallMovement(ball, ballDirX, ballDirY)
        
        #Mostramos el nombre del juego, actualizamos el titulo y actualizamos el framerate
        pygame.display.set_caption('Python - Pygame Simple Arcade Game')
        pygame.display.update()
        clock.tick(fps) 

#Llamamos a la función main
main()
