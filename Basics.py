import pygame
import random

xres = 800
yres = 600

gameDisplay = pygame.display.set_mode((xres, yres))

backgroundImage = pygame.image.load("background.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (xres, yres))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

playerWidth = 100
playerHeight = 10
playerXpos = xres/2
playerYpos = yres - 50
playerMidXpos = (2*playerXpos+playerWidth)/2

oppoWidth = 100
oppoHeight = 10
oppoXpos = xres/2
oppoYpos = 50
oppoMidXpos = (2 * oppoXpos + oppoWidth) / 2

ballXpos = xres/2
ballYpos = yres/2
ballRadius = 5
ballXspeed = 5
ballYspeed = 5

playerScore = 0
oppoScore = 0
