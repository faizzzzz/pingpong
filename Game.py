import pygame
import random
import Basics as sb
from Menu import menu
from Screen_Update import screen_update
from Player import player
from Ball import ball
from Opponent import oppo
from ScoreKeep import score

global gameRun, playerXpos, playerYpos

def game():

    step = 10

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sb.playerXpos += step

            if event.key == pygame.K_LEFT:
                sb.playerXpos -= step

            if event.key == pygame.K_UP:
                sb.playerYpos -= step

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

if __name__ == "__main__":
    while True:

        if menu.showMenu == True:
            menu.menu()

        if menu.gameRun == True:
            ball.move()
            player.movement()
            player.motion()
            oppo.movement()
            score()

            screen_update()
