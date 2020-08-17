import pygame

black = (0, 0, 0)

pygame.font.init()
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, xpos, ypos, size, display, color=black):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((xpos),(ypos))

    display.blit(TextSurf, TextRect)