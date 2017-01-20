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
        pygame.display.set_caption("The Euromast")
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
            #opslaan spelerknoppen
            if speler1knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 160, 30, 30])
                pygame.display.update()
            if speler2knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 260, 30, 30])
                pygame.display.update()
            if speler3knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 360, 30, 30])
                pygame.display.update()
            if speler4knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 460, 30, 30])
                pygame.display.update()
            #opslaan pcknoppen
            if pc1knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 160, 30, 30])
                pygame.display.update() 
            if pc2knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 260, 30, 30])
                pygame.display.update()
            if pc3knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 360, 30, 30])
                pygame.display.update()
            if pc4knop == 1:
                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 460, 30, 30]) 
                pygame.display.update()
            pygame.display.set_caption("The Euromast - Aantal Spelers")
            pygame.display.update()
    def spel():
        
        
            screen.fill(WHITE)
            screen.blit(text4, (310, 50, 400, 50)) 
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 150, 400, 50]) 
            
            pygame.display.flip()

speler1knop = 0
speler2knop = 0
speler3knop = 0
speler4knop = 0
pc1knop = 0
pc2knop = 0
pc3knop = 0
pc4knop = 0

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
                subdone = False
                while not subdone:
                    for event in pygame.event.get(): 
                        
                        if event.type== pygame.MOUSEBUTTONDOWN:
                            mx, my = pygame.mouse.get_pos()
                            #speler buttons veranderen in kleur
                            if my > 160 and my < 190 and mx < screenWidth/2 - 410  and mx > screenWidth/2 - 440: #button1speler wordt kleur
                                if pc1knop == 1:
                                    pc1knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 160, 30, 30])
                                    print(str(pc1knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 160, 30, 30])
                                speler1knop = 1 
                                print(str(speler1knop))
                                pygame.display.update()
                            if my > 260 and my < 290 and mx < screenWidth/2 - 410  and mx > screenWidth/2 - 440: #button2speler wordt kleur
                                if pc2knop == 1:
                                    pc2knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 260, 30, 30])
                                    print(str(pc2knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 260, 30, 30])
                                speler2knop = speler2knop + 1 
                                print(str(speler2knop))
                                pygame.display.update()
                            if my > 360 and my < 390 and mx < screenWidth/2 - 410  and mx > screenWidth/2 - 440: #button3speler wordt kleur
                                if pc3knop == 1:
                                    pc3knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 360, 30, 30])
                                    print(str(pc3knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 360, 30, 30])
                                speler3knop = speler3knop + 1 
                                print(str(speler3knop))
                                pygame.display.update()
                            if my > 460 and my < 490 and mx < screenWidth/2 - 410  and mx > screenWidth/2 - 440: #button4speler wordt kleur
                                if pc4knop == 1:
                                    pc4knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 350, 460, 30, 30])
                                    print(str(pc4knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 440, 460, 30, 30])
                                speler4knop = speler4knop + 1 
                                print(str(speler4knop))
                                pygame.display.update()
                            


                            #pc buttons veranderen kleur
                            if my > 160 and my < 190 and mx < screenWidth/2 - 320  and mx > screenWidth/2 - 350: #pc1speler wordt kleur
                                if speler1knop == 1:
                                    speler1knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 160, 30, 30])
                                    print(str(speler1knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 160, 30, 30])
                                pc1knop = 1 
                                print(str(pc1knop))
                                pygame.display.update()
                            if my > 260 and my < 290 and mx < screenWidth/2 - 320  and mx > screenWidth/2 - 350: #pc2speler wordt kleur
                                if speler2knop == 1:
                                    speler2knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 260, 30, 30])
                                    print(str(speler2knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 260, 30, 30])
                                pc2knop = 1 
                                print(str(pc2knop))
                                pygame.display.update()
                            if my > 360 and my < 390 and mx < screenWidth/2 - 320  and mx > screenWidth/2 - 350: #pc3speler wordt kleur
                                if speler3knop == 1:
                                    speler3knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 360, 30, 30])
                                    print(str(speler3knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 360, 30, 30])
                                pc3knop = 1 
                                print(str(pc3knop))
                                pygame.display.update()
                            if my > 460 and my < 490 and mx < screenWidth/2 - 320  and mx > screenWidth/2 - 350: #pc4speler wordt kleur
                                if speler4knop == 1:
                                    speler4knop = 0
                                    pygame.draw.rect(screen, BLACK, [screenWidth/2 - 440, 460, 30, 30])
                                    print(str(speler4knop))
                                pygame.draw.rect(screen, RED, [screenWidth/2 - 350, 460, 30, 30])
                                pc4knop = 1 
                                print(str(pc4knop))
                                pygame.display.update()
                           
                            #terug knop  
                            if my > 530 and my < 570 and mx < screenWidth/2 - 350 and mx > screenWidth/2 - 440: 
                                bordspel.start()                             
                                pygame.display.update()
                                subdone = True #ga uit loop
                        if event.type == pygame.QUIT: #Ga uit loop
                            subdone = True
                            done = True
                
                pygame.display.flip()
                pygame.display.update()
            
            if my > 350 and my < 400 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
                quit()
            
            
    
# Be IDLE friendly
pygame.quit()
quit()