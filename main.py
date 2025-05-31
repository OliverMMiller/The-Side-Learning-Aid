import sys
import pygame
import time
from pygame.locals import QUIT

background = pygame.image.load("theSide.jpg")

SCREEN_WIDTH = background.get_width()
SCREEN_HEIGHT = background.get_height()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), (pygame.FULLSCREEN | pygame.SCALED))  # | pygame.NOFRAME  pygame.RESIZABLE
pygame.display.set_caption('Piping the side learning aid')

print("Screen size: ", DISPLAYSURF.get_size())


LinePos = 0
startOffset = 180
lineTravel = 555 - startOffset

totalTime = 12 #seconds

FPS = 47#int(lineTravel // totalTime) # frames per second
FramePerSec = pygame.time.Clock()

countDownFrames = 3 # seconds

pygame.font.init()  # Initialize font module
font = pygame.font.Font(None, 100)  # Font for countdown text


def quitFunc() -> None:
    """
    Quits the program when the 'Quit' button is pressed.
    """
    pygame.quit()
    sys.exit()
    
pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.WINDOWCLOSE,
                          pygame.WINDOWFOCUSGAINED, pygame.WINDOWFOCUSLOST, 
                          pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP))


while __name__ == "__main__":
    for event in pygame.event.get():
        if event.type == QUIT:  # if program exited then end program
            quitFunc()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitFunc()
            elif event.key == pygame.K_SPACE:
                  countDownFrames = FPS * 3 # seconds
        elif event.type == pygame.WINDOWCLOSE:
            quitFunc()


    DISPLAYSURF.blit(background, (0, 0))
    
    
    countDownTime = int(countDownFrames // FPS + 1)

    if countDownFrames == 0:
        LinePos = 0
    elif countDownFrames > 0:
        text_bitmap = font.render(str(countDownTime), True, (0, 0, 0))
        DISPLAYSURF.blit(text_bitmap, (500, 500))
        LinePos = 0
        pygame.draw.line(DISPLAYSURF, (0,0,0), (LinePos + startOffset, 170), (LinePos + startOffset, 280), width=2)
    if countDownFrames <= 0:
        if LinePos < lineTravel + startOffset:
            pygame.draw.line(DISPLAYSURF, (0,0,0), (LinePos + startOffset, 170), (LinePos + startOffset, 280), width=2)
            LinePos += 1
    countDownFrames -= 1
        

    pygame.display.update()
    FramePerSec.tick(FPS)