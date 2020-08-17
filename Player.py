import pygame
import Basics as sb

class Player:
    def __init__(self):
        self.status = (0,1,0)   # moving left, stationary, moving right
        self.step = 7
        self.wallBound = False

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.status = (0,0,1)

                if event.key == pygame.K_LEFT:
                    self.status = (1,0,0)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYUP:
                self.status = (0,1,0)

            if (sb.playerXpos <= 0) or (sb.playerXpos >= (sb.xres - sb.playerWidth)):
                self.wallBound = True

    def motion(self):
        self.INCR = self.step

        if self.status == (0,0,1) and sb.playerXpos < sb.xres - sb.playerWidth:
            sb.playerXpos += self.INCR

        if self.status == (1, 0, 0) and sb.playerXpos > 0:
            sb.playerXpos -= self.INCR

        if self.status == (0, 0, 1):
            self.INCR = 0


player = Player()
