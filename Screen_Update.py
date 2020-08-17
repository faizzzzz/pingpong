import pygame
import Basics as sb
from message import message_display

def screen_update():

    clock = pygame.time.Clock()
    sb.gameDisplay.blit(sb.backgroundImage, (0, 0))

    pygame.draw.rect(sb.gameDisplay, sb.black, (sb.playerXpos,sb.playerYpos,sb.playerWidth, sb.playerHeight))
    pygame.draw.circle(sb.gameDisplay, sb.black, (int((2 * sb.playerXpos + sb.playerWidth) / 2), sb.playerYpos),sb.ballRadius)

    pygame.draw.rect(sb.gameDisplay, sb.black, (sb.oppoXpos, sb.oppoYpos, sb.oppoWidth, sb.oppoHeight))
    pygame.draw.circle(sb.gameDisplay, sb.black, (int((2 * sb.oppoXpos + sb.oppoWidth) / 2), sb.oppoYpos + sb.oppoHeight),sb.ballRadius, )

    pygame.draw.circle(sb.gameDisplay, sb.black, (int(sb.ballXpos), int(sb.ballYpos)), sb.ballRadius, )


    pygame.draw.rect(sb.gameDisplay, sb.red, (0, 0, sb.xres, sb.oppoYpos))
    pygame.draw.rect(sb.gameDisplay, sb.green, (0, sb.playerYpos + sb.playerHeight, sb.xres, sb.yres))
    oppoScoreText = "Opponent: " + str(sb.oppoScore)
    playerScoreText = "Player: " + str(sb.playerScore)
    message_display(oppoScoreText, 50, sb.oppoYpos/2, 15, sb.gameDisplay, sb.white)
    message_display(playerScoreText, 50, sb.xres - 220, 15, sb.gameDisplay, sb.black)

    clock.tick(60)
    pygame.display.update()

