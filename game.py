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
screenWidth = 1000
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("The Euromast")
 
#Loop until the user clicks the close button.
clock = pygame.time.Clock()
font = pygame.font.SysFont( "Times New Roman, Arial", 30)
text = font.render("Start", True, WHITE)
text2 = font.render("Aantal Spelers", True, WHITE)
text3 = font.render("Exit", True, WHITE)
text4 = font.render("Geef uw naam", True, WHITE)
text5 = font.render("Vink het aantal spelers aan", True, BLACK)
text6 = font.render("Speler     Pc               Geef uw naam", True, BLACK)
text7 = font.render("Terug", True, WHITE)
class bordspel:
    def start():
        screen.fill(WHITE)
        mx, my = pygame.mouse.get_pos()
        if my > 150 and my < 200 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 150, 400, 50]) 
        else:
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 150, 400, 50]) 
        if my > 250 and my < 300 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 250, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 250, 400, 50])
        if my > 350 and my < 400 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 350, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 350, 400, 50])

        screen.blit(text, [screenWidth/2 - 30, 157, 400, 50])
        screen.blit(text2, [screenWidth/2- 85, 257, 400, 50])
        screen.blit(text3, [screenWidth/2 - 25, 357, 400, 50])

    def aantalspelers():
            screen.fill(WHITE)
            #geef uw naam vakjes
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 150, 300, 50]) 
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 250, 300, 50]) 
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 350, 300, 50]) 
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 450, 300, 50])
            #speler vakjes
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 160, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 260, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 360, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 460, 30, 30])
            #pc vakjes
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 160, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 260, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 360, 30, 30])
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 460, 30, 30]) 
            #teksten    
            screen.blit(text5, [screenWidth/2 - 150, 50, 400, 50])
            screen.blit(text6, [screenWidth/2 - 460, 100, 400, 50])
            #terug knop
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 530, 90, 40])
            screen.blit(text7, [screenWidth/2 - 430, 530, 90, 800])
            
            pygame.display.update()
    def spel():
        
        
            screen.fill(WHITE)
            screen.blit(text4, (310, 50, 400, 50)) 
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 150, 400, 50]) 
            
            pygame.display.flip()


done = False
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True
    
    # Clear the screen and set the screen background
    
    
    #draw the buttons 
    bordspel.start()
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
            if my > 150 and my < 200 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
                bordspel.spel()
                done = False
                while not done:
                    for event in pygame.event.get(): # User did something
                        if event.type == pygame.QUIT: # If user clicked close
                            done = True
                pygame.display.flip()
                pygame.display.update()
            if my > 250 and my < 300 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
                bordspel.aantalspelers()
                done = False
                while not done:
                    for event in pygame.event.get(): # User did something
                        if event.type== pygame.MOUSEBUTTONDOWN:
                            mx, my = pygame.mouse.get_pos()
                            if my > 530 and my < 570 and mx < screenWidth/2 - 350 and mx > screenWidth/2 - 440:
                                bordspel.start()                                
                                pygame.display.update()
                        if event.type == pygame.QUIT: # If user clicked close
                            done = True
                pygame.display.flip()
                pygame.display.update()
            if my > 350 and my < 400 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
                quit()
            
            
    
# Be IDLE friendly
pygame.quit()
quit()