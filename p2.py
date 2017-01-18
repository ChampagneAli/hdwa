# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
GREY =  ( 80,  80,  80)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [800, 400]
screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)
pygame.display.set_caption("The Euromast")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont( "Times New Roman, Arial", 30)
text = font.render("Start", True, WHITE)
text2 = font.render("Aantal Spelers", True, WHITE)
text3 = font.render("Exit", True, WHITE)
class bordspel:
    def start(self):
        screen.fill(WHITE)
        mx, my = pygame.mouse.get_pos()
        if my > 50 and my < 100 and mx < 600 and mx > 200:
            pygame.draw.rect(screen, GREY, [200, 50, 400, 50]) 
        else:
            pygame.draw.rect(screen, BLACK, [200, 50, 400, 50]) 
        if my > 150 and my < 200 and mx < 600 and mx > 200:
            pygame.draw.rect(screen, GREY, [200, 150, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [200, 150, 400, 50])
        if my > 250 and my < 300 and mx < 600 and mx > 200:
            pygame.draw.rect(screen, GREY, [200, 250, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [200, 250, 400, 50])
        screen.blit(text, (370, 50, 400, 50))
        screen.blit(text2, (310, 150, 400, 50))
        screen.blit(text3, (370, 250, 400, 50))
    def speelbord():
        while True:
            screen.fill(RED)
            
            pygame.display.flip()


g = bordspel()


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
    
    # Clear the screen and set the screen background
    
    
    #draw the buttons 
    g.start()
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    caption = 'PyGuts - A Pygame front-end based on the python-spine Runtime' 
     # Flag that we are done so we exit this loop
    if event.type== pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if my > 50 and my < 100 and mx < 600 and mx > 200:
                bordspel.speelbord()
                pygame.display.flip()
                pygame.display.update()
            if my > 150 and my < 200 and mx < 600 and mx > 200:
                print ("Tweede Knop")
            if my > 250 and my < 300 and mx < 600 and mx > 200:
                print ("Derde Knop")
 
    
# Be IDLE friendly
pygame.quit()