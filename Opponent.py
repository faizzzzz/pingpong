import pygame
import Basics as sb

class Opponent:
    def __init__(self):
        self.step = 5
        self.INCR = 0

    def movement(self):
        self.oppoBallDist = sb.ballXpos - ((2 * sb.oppoXpos + sb.oppoWidth) / 2)

        if self.oppoBallDist > 0 and sb.oppoXpos + sb.oppoWidth < sb.xres:       # oppo is at left and ball is at right
            self.INCR = self.step       # moving right

        if self.oppoBallDist < 0 and sb.oppoXpos > 0:       # oppos is at right and ball is at left
            self.INCR = -self.step      # moving left

        if sb.oppoXpos < 0:
            self.INCR = self.step

        if sb.oppoXpos + sb.oppoWidth > sb.xres:
            self.INCR = -self.step


        sb.oppoXpos += self.INCR


oppo = Opponent()
