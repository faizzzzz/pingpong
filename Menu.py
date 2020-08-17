import pygame
from message import message_display
import Basics as sb

class PauseMenu:
    def __init__(self):
        self.showMenu = True
        self.gameRun = False

    def menu(self):
        sb.gameDisplay.fill(sb.white)
        message_display("Welcome", sb.xres/2, sb.yres/2 + 100, 25, sb.gameDisplay)
        message_display("Press Enter to play or Esc to exit.", sb.xres/2, sb.yres/2 + 50, 25, sb.gameDisplay)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.showMenu = False
                    self.gameRun = True

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


menu = PauseMenu()
