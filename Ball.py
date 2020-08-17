import pygame
import Basics as sb
import math, random

class Ball:
    def __init__(self):
        self.xspeed = 5
        self.yspeed = 5
        self.angle = 0
        self.ballVel = 0
        self.strikeAngleFactor = 5
        self.factor = 0
        self.xINCR = 0

        self.yINCR = -self.yspeed
        self.xINCR = self.xspeed

    def move(self):

        if sb.ballYpos > sb.playerYpos and sb.ballYpos < sb.playerYpos + sb.playerHeight and sb.ballXpos > sb.playerXpos and sb.ballXpos < sb.playerXpos + sb.playerWidth:
            self.yINCR = -self.yspeed

            self.playerMidXpos = (2 * sb.playerXpos+sb.playerWidth)/2
                
            
            if sb.ballXpos > self.playerMidXpos:
                

                if self.xINCR > 0:
                    self.factor = ((sb.ballXpos - self.playerMidXpos) / sb.playerWidth)
                    self.xINCR = self.xspeed + self.factor * self.strikeAngleFactor

                else:
                    self.factor = 0
                    self.xINCR = -(self.xspeed + self.factor * self.strikeAngleFactor)


            if sb.ballXpos < self.playerMidXpos:

                if self.xINCR > 0:
                    self.factor = 0
                    self.xINCR = (self.xspeed + self.factor * self.strikeAngleFactor)

                else:
                    self.factor = ((self.playerMidXpos - sb.ballXpos) / sb.playerWidth)

                    self.xINCR = -(self.xspeed + self.factor * self.strikeAngleFactor)
                    

        if sb.ballYpos > sb.oppoYpos and sb.ballYpos < sb.oppoYpos + sb.oppoHeight and sb.ballXpos > sb.oppoXpos and sb.ballXpos < sb.oppoXpos + sb.oppoWidth:
            self.yINCR = self.yspeed

            self.oppoMidXpos = (2 * sb.oppoXpos + sb.oppoWidth) / 2

            if sb.ballXpos > self.oppoMidXpos:
                self.factor = ((sb.ballXpos - self.oppoMidXpos) / sb.oppoWidth)
                self.xINCR = self.xspeed + self.factor * self.strikeAngleFactor

            if sb.ballXpos < self.oppoMidXpos:
                self.factor = ((self.oppoMidXpos - sb.ballXpos) / sb.oppoWidth)

                if self.xINCR > 0:
                    self.xINCR = -(self.xspeed + self.factor * self.strikeAngleFactor)

        if sb.ballXpos > sb.xres - sb.ballRadius:
            self.xINCR = -self.xspeed

        if sb.ballXpos < 0:
            self.xINCR = self.xspeed

        sb.ballXpos += self.xINCR
        sb.ballYpos += self.yINCR



ball = Ball()
