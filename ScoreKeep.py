import Basics as sb
import time, random
from Ball import ball


def resetBall():
    sb.ballXpos = sb.xres/2
    # sb.ballYpos = sb.yres/2
    sb.playerXpos = sb.xres/2
    sb.oppoXpos = sb.xres/2

    ball.xINCR = random.choice([-1, 1]) * ball.xspeed

    time.sleep(2)


def score():
    if sb.ballYpos > sb.xres:
        sb.oppoScore += 1
        sb.ballYpos = sb.oppoYpos + sb.oppoHeight
        resetBall()

    if sb.ballYpos < 0:
        sb.playerScore += 1
        sb.ballYpos = sb.playerYpos
        resetBall()