from pygame.locals import *
import pygame, string, random
from math import pi
pygame.init()

# Background image is set as 'bg'
bg = pygame.image.load("FOTO achtergrond.png")
vink = pygame.image.load("FOTO groen vinkje.png")
kruis = pygame.image.load("FOTO rood kruisje.png")
arrow = pygame.image.load("FOTO arrow.png")
speelbord_bg = pygame.image.load("FOTO speelbord.png")

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
GREY =  ( 80,  80,  80)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 100)
LIGHT_BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#\aantalspelers startvalue knoppen
speler1knop = 0
speler2knop = 0
speler3knop = 0
speler4knop = 0
pc1knop = 0
pc2knop = 0
pc3knop = 0
pc4knop = 0

               #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ConfigError(KeyError): pass
class Config:
    """ A utility for configuration """
    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
            else: exec('self.'+key[0]+' = '+key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(key+' not expected as option')
class Input:
    """ A text input for pygame apps """
    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'], ['font', 'pygame.font.Font(None, 32)'],
                              ['color', '(0,0,0)'], ['restricted', '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''],
                              ['maxlength', '-1'], ['prompt', '\'\''])
        self.x = self.options.x; self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.restricted = self.options.restricted
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt; self.value = ''
        self.shifted = False

    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt+self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self, events):
        """ Update the input based on passed events """
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_SPACE: self.value += ' '
                if not self.shifted:
                    if event.key == K_a and 'a' in self.restricted: self.value += 'a'
                    elif event.key == K_b and 'b' in self.restricted: self.value += 'b'
                    elif event.key == K_c and 'c' in self.restricted: self.value += 'c'
                    elif event.key == K_d and 'd' in self.restricted: self.value += 'd'
                    elif event.key == K_e and 'e' in self.restricted: self.value += 'e'
                    elif event.key == K_f and 'f' in self.restricted: self.value += 'f'
                    elif event.key == K_g and 'g' in self.restricted: self.value += 'g'
                    elif event.key == K_h and 'h' in self.restricted: self.value += 'h'
                    elif event.key == K_i and 'i' in self.restricted: self.value += 'i'
                    elif event.key == K_j and 'j' in self.restricted: self.value += 'j'
                    elif event.key == K_k and 'k' in self.restricted: self.value += 'k'
                    elif event.key == K_l and 'l' in self.restricted: self.value += 'l'
                    elif event.key == K_m and 'm' in self.restricted: self.value += 'm'
                    elif event.key == K_n and 'n' in self.restricted: self.value += 'n'
                    elif event.key == K_o and 'o' in self.restricted: self.value += 'o'
                    elif event.key == K_p and 'p' in self.restricted: self.value += 'p'
                    elif event.key == K_q and 'q' in self.restricted: self.value += 'q'
                    elif event.key == K_r and 'r' in self.restricted: self.value += 'r'
                    elif event.key == K_s and 's' in self.restricted: self.value += 's'
                    elif event.key == K_t and 't' in self.restricted: self.value += 't'
                    elif event.key == K_u and 'u' in self.restricted: self.value += 'u'
                    elif event.key == K_v and 'v' in self.restricted: self.value += 'v'
                    elif event.key == K_w and 'w' in self.restricted: self.value += 'w'
                    elif event.key == K_x and 'x' in self.restricted: self.value += 'x'
                    elif event.key == K_y and 'y' in self.restricted: self.value += 'y'
                    elif event.key == K_z and 'z' in self.restricted: self.value += 'z'
                    elif event.key == K_0 and '0' in self.restricted: self.value += '0'
                    elif event.key == K_1 and '1' in self.restricted: self.value += '1'
                    elif event.key == K_2 and '2' in self.restricted: self.value += '2'
                    elif event.key == K_3 and '3' in self.restricted: self.value += '3'
                    elif event.key == K_4 and '4' in self.restricted: self.value += '4'
                    elif event.key == K_5 and '5' in self.restricted: self.value += '5'
                    elif event.key == K_6 and '6' in self.restricted: self.value += '6'
                    elif event.key == K_7 and '7' in self.restricted: self.value += '7'
                    elif event.key == K_8 and '8' in self.restricted: self.value += '8'
                    elif event.key == K_9 and '9' in self.restricted: self.value += '9'
                    elif event.key == K_BACKQUOTE and '`' in self.restricted: self.value += '`'
                    elif event.key == K_MINUS and '-' in self.restricted: self.value += '-'
                    elif event.key == K_EQUALS and '=' in self.restricted: self.value += '='
                    elif event.key == K_LEFTBRACKET and '[' in self.restricted: self.value += '['
                    elif event.key == K_RIGHTBRACKET and ']' in self.restricted: self.value += ']'
                    elif event.key == K_BACKSLASH and '\\' in self.restricted: self.value += '\\'
                    elif event.key == K_SEMICOLON and ';' in self.restricted: self.value += ';'
                    elif event.key == K_QUOTE and '\'' in self.restricted: self.value += '\''
                    elif event.key == K_COMMA and ',' in self.restricted: self.value += ','
                    elif event.key == K_PERIOD and '.' in self.restricted: self.value += '.'
                    elif event.key == K_SLASH and '/' in self.restricted: self.value += '/'
                       
                elif self.shifted:
                    if event.key == K_a and 'A' in self.restricted: self.value += 'A'
                    elif event.key == K_b and 'B' in self.restricted: self.value += 'B'
                    elif event.key == K_c and 'C' in self.restricted: self.value += 'C'
                    elif event.key == K_d and 'D' in self.restricted: self.value += 'D'
                    elif event.key == K_e and 'E' in self.restricted: self.value += 'E'
                    elif event.key == K_f and 'F' in self.restricted: self.value += 'F'
                    elif event.key == K_g and 'G' in self.restricted: self.value += 'G'
                    elif event.key == K_h and 'H' in self.restricted: self.value += 'H'
                    elif event.key == K_i and 'I' in self.restricted: self.value += 'I'
                    elif event.key == K_j and 'J' in self.restricted: self.value += 'J'
                    elif event.key == K_k and 'K' in self.restricted: self.value += 'K'
                    elif event.key == K_l and 'L' in self.restricted: self.value += 'L'
                    elif event.key == K_m and 'M' in self.restricted: self.value += 'M'
                    elif event.key == K_n and 'N' in self.restricted: self.value += 'N'
                    elif event.key == K_o and 'O' in self.restricted: self.value += 'O'
                    elif event.key == K_p and 'P' in self.restricted: self.value += 'P'
                    elif event.key == K_q and 'Q' in self.restricted: self.value += 'Q'
                    elif event.key == K_r and 'R' in self.restricted: self.value += 'R'
                    elif event.key == K_s and 'S' in self.restricted: self.value += 'S'
                    elif event.key == K_t and 'T' in self.restricted: self.value += 'T'
                    elif event.key == K_u and 'U' in self.restricted: self.value += 'U'
                    elif event.key == K_v and 'V' in self.restricted: self.value += 'V'
                    elif event.key == K_w and 'W' in self.restricted: self.value += 'W'
                    elif event.key == K_x and 'X' in self.restricted: self.value += 'X'
                    elif event.key == K_y and 'Y' in self.restricted: self.value += 'Y'
                    elif event.key == K_z and 'Z' in self.restricted: self.value += 'Z'
                    elif event.key == K_0 and ')' in self.restricted: self.value += ')'
                    elif event.key == K_1 and '!' in self.restricted: self.value += '!'
                    elif event.key == K_2 and '@' in self.restricted: self.value += '@'
                    elif event.key == K_3 and '#' in self.restricted: self.value += '#'
                    elif event.key == K_4 and '$' in self.restricted: self.value += '$'
                    elif event.key == K_5 and '%' in self.restricted: self.value += '%'
                    elif event.key == K_6 and '^' in self.restricted: self.value += '^'
                    elif event.key == K_7 and '&' in self.restricted: self.value += '&'
                    elif event.key == K_8 and '*' in self.restricted: self.value += '*'
                    elif event.key == K_9 and '(' in self.restricted: self.value += '('
                    elif event.key == K_BACKQUOTE and '~' in self.restricted: self.value += '~'
                    elif event.key == K_MINUS and '_' in self.restricted: self.value += '_'
                    elif event.key == K_EQUALS and '+' in self.restricted: self.value += '+'
                    elif event.key == K_LEFTBRACKET and '{' in self.restricted: self.value += '{'
                    elif event.key == K_RIGHTBRACKET and '}' in self.restricted: self.value += '}'
                    elif event.key == K_BACKSLASH and '|' in self.restricted: self.value += '|'
                    elif event.key == K_SEMICOLON and ':' in self.restricted: self.value += ':'
                    elif event.key == K_QUOTE and '"' in self.restricted: self.value += '"'
                    elif event.key == K_COMMA and '<' in self.restricted: self.value += '<'
                    elif event.key == K_PERIOD and '>' in self.restricted: self.value += '>'
                    elif event.key == K_SLASH and '?' in self.restricted: self.value += '?'
        
        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
        return self.value
               #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
               #Deze 3 klassen verkleinen -> (nodig voor user textinput)

#textboxen voor aantalspelers
n1 = Input(maxlength=15, color=(0,0,0), prompt='')
n2 = Input(maxlength=15, color=(0,0,0), prompt='')
n3 = Input(maxlength=15, color=(0,0,0), prompt='')
n4 = Input(maxlength=15, color=(0,0,0), prompt='')

#nodig om naam te kunnen herinneren
herinner1 = 0
herinner2 = 0
herinner3 = 0
herinner4 = 0

#scores bijhouden
n1score = 0
n2score = 0
n3score = 0
n4score = 0

#naam default
n1var = 'Geen naam'
n2var = 'Geen naam'
n3var = 'Geen naam'
n4var = 'Geen naam'

# Set the height and width of the screen
screenWidth = 1000
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("The Euromast")
 
#some variables
clock = pygame.time.Clock()
fontsmall = pygame.font.SysFont("Times New Roman, Arial", 20)
font = pygame.font.SysFont("Times New Roman, Arial", 30)
fontmedium = pygame.font.SysFont("Times New Roman, Arial", 50)
fontlarge = pygame.font.SysFont("Times New Roman, Arial", 70)
text = font.render("Start", True, WHITE)
text2 = font.render("Aantal Spelers", True, WHITE)
text3 = font.render("Exit", True, WHITE)
text4 = font.render("Geef uw naam", True, WHITE)
text5 = font.render("Vink het aantal spelers aan", True, BLACK)
text6 = font.render("Speler     Pc               Geef uw naam", True, BLACK)
text7 = font.render("Terug", True, WHITE)
text8 = font.render("hier komt het spel", True, BLACK)
text9 = fontlarge.render("The Euromast", True, BLUE)
text10 = font.render("Vink minimaal twee spelers/PC's aan.", True, RED)
text11 = font.render("Vink minimaal één speler aan.", True, RED)
text12 = fontsmall.render("Scores:", True, BLUE)
#text13-16 zijn bezet

#begin values voor de start error
error10 = 0 
error11 = 0


                                                                      #DEFINED SCREENS AND FUNCTIONS

class bordspel: 
    def naam(txtbx):
        bordspel.aantalspelers()
        if txtbx == n1:
            txtbx.set_pos(screenWidth/2 - 180, 163)
        elif txtbx == n2:
            txtbx.set_pos(screenWidth/2 - 180, 263)
        elif txtbx == n3:
            txtbx.set_pos(screenWidth/2 - 180, 363)
        elif txtbx == n4:
            txtbx.set_pos(screenWidth/2 - 180, 463)
        txtbx.update(events)
        txtbx.draw(screen)

    def start():
        screen.fill(WHITE)
        screen.blit(bg,(0,0)) #draw background image
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
        screen.blit(text, [screenWidth/2 - 30, 157])
        screen.blit(text2, [screenWidth/2- 85, 257])
        screen.blit(text3, [screenWidth/2 - 25, 357])
        screen.blit(text9, [300, 20])
        #geef error als op start geklikt word
        if error10 == 1:
            screen.blit(text10, [15, 95]) #start-error
            screen.blit(arrow,(0,0))
        if error11 == 1:
            screen.blit(text11, [20, 100]) #start-error
            screen.blit(arrow,(0,0))
        
    def aantalspelers():
        screen.blit(bg,(0,0)) #draw background image
        #geef uw naam vakjes
        pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 150, 300, 50]) 
        pygame.draw.rect(screen, WHITE, [screenWidth/2 - 193, 155, 285, 40]) 
        pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 250, 300, 50]) 
        pygame.draw.rect(screen, WHITE, [screenWidth/2 - 193, 255, 285, 40]) 
        pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 350, 300, 50]) 
        pygame.draw.rect(screen, WHITE, [screenWidth/2 - 193, 355, 285, 40]) 
        pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 450, 300, 50])
        pygame.draw.rect(screen, WHITE, [screenWidth/2 - 193, 455, 285, 40])
        #teksten    
        screen.blit(text5, [screenWidth/2 - 150, 35])
        screen.blit(text6, [screenWidth/2 - 460, 100])
        #terug knop
        pygame.draw.rect(screen, BLUE, [screenWidth/2 - 440, 530, 90, 40])
        screen.blit(text7, [screenWidth/2 - 430, 530, 90, 800]) 
        #opgeslagen spelervakjes
        if speler1knop == 1:    screen.blit(vink,(60, 160))
        else:   screen.blit(kruis,(60, 160))
        if speler2knop == 1:    screen.blit(vink,(60, 260))
        else:   screen.blit(kruis,(60, 260))
        if speler3knop == 1:    screen.blit(vink,(60, 360))
        else:   screen.blit(kruis,(60, 360))
        if speler4knop == 1:    screen.blit(vink,(60, 460))
        else:   screen.blit(kruis,(60, 460))
        #opslaan pcknoppen
        if pc1knop == 1:    screen.blit(vink,(150, 160))
        else: screen.blit(kruis,(150, 160))
        if pc2knop == 1:    screen.blit(vink,(150, 260))
        else: screen.blit(kruis,(150, 260))
        if pc3knop == 1:    screen.blit(vink,(150, 360))
        else: screen.blit(kruis,(150, 360))
        if pc4knop == 1:    screen.blit(vink,(150, 460)) 
        else: screen.blit(kruis,(150, 460))
        #opgeslagen naam schrijven
        if herinner1 == 1:
            if n1var != '' or n1var != None:
                n1.draw(screen)
        if herinner2 == 1:
            if n2var != '' or n2var != None:
                n2.draw(screen)
        if herinner3 == 1:
            if n3var != '' or n3var != None:
                n3.draw(screen)
        if herinner4 == 1:
            if n4var != '' or n4var != None:
                n4.draw(screen)

        pygame.display.set_caption("The Euromast - Aantal Spelers")

    def spel():
        screen.blit(speelbord_bg,(0,0)) #draw background image
        pygame.display.set_caption("The Euromast - Start!")
        #scores
        text13 = fontsmall.render(n1var + ": " + str(n1score), True, BLUE)
        text14 = fontsmall.render(n2var + ": " + str(n2score), True, BLUE)
        text15 = fontsmall.render(n3var + ": " + str(n3score), True, BLUE)
        text16 = fontsmall.render(n4var + ": " + str(n4score), True, BLUE)
        screen.blit(text12, [5, 5])
        if speler1knop == 1 or pc1knop ==1:
            screen.blit(text13, [15, 23])
        if speler2knop == 1 or pc2knop == 1:
            screen.blit(text14, [15, 41])
        if speler3knop == 1 or pc3knop == 1:
            screen.blit(text15, [15, 59])
        if speler4knop == 1 or pc4knop == 1:
            screen.blit(text16, [15, 77])

        aantal = speler1knop + speler2knop + speler3knop + speler4knop + pc1knop + pc2knop + pc3knop + pc4knop
        randomdobbel = int(random.randint(1,aantal))
        print(randomdobbel)
        if randomdobbel == 1:
            print(n1var)
        if randomdobbel == 2:
	        print(n2var)
        if randomdobbel == 3:
	        print(n3var)
        if randomdobbel == 4:
	        print(n4var)





                                                                      #THE MAIN WHILE LOOP 
done = False
while not done:
    for event in pygame.event.get(): # User input kan worden opgehaald -> print(event)
        if event.type == pygame.QUIT: # If user clicked close -> exit gameloop
            done = True
    
    bordspel.start()
    pygame.display.update()
    
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    (left_mouse, middle_mouse, right_mouse) = pygame.mouse.get_pressed() #user input on the mouse (boolean int)
    if left_mouse == 1:
            mx, my = pygame.mouse.get_pos()
            if 150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #'start'
                if speler1knop + speler2knop + speler3knop + speler4knop + pc1knop + pc2knop + pc3knop + pc4knop < 2:
                    error10 = 1
                elif speler1knop + speler2knop + speler3knop + speler4knop == 0:
                    error11 = 1
                else:
                    if pc1knop == 1:
                        n1var += ' (PC)'
                    if pc2knop == 1:
                        n2var += ' (PC)'
                    if pc3knop == 1:
                        n3var += ' (PC)'
                    if pc4knop == 1:
                        n4var += ' (PC)'
                    bordspel.spel()
                    pygame.display.update()
                    done = False
                    while not done:
                        for event in pygame.event.get(): # User input kan worden opgehaald -> print(event)
                            if event.type == pygame.QUIT:
                                done = True
            if 250 < my < 300 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #'aantal spelers'
                error10 = 0
                error11 = 0
                bordspel.aantalspelers()
                pygame.display.update()
                subdone = False
                while not subdone:
                    for event in pygame.event.get(): # User input kan worden opgehaald -> print(event)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1: # 1links 2midden 3rechts 4scrollup 5scrolldown
                                mx, my = pygame.mouse.get_pos()
                                if 530 < my < 570 and screenWidth/2 - 350 > mx > screenWidth/2 - 440: #'aantalspelers'\'terug'
                                    bordspel.start()                   
                                    pygame.display.update()
                                    subdone = True

                                #speler buttons veranderen in kleur
                                if 160 < my < 190 and screenWidth/2 - 410 > mx > screenWidth/2 - 440: #button1speler wordt kleur
                                    if pc1knop == 1:                                        
                                        pc1knop = 0
                                        screen.blit(kruis,(150, 160))
                                    if speler1knop == 0:
                                        screen.blit(vink,(60, 160))
                                        speler1knop = 1
                                    else:
                                        speler2knop == 0
                                        screen.blit(kruis,(60, 260))
                                        pc2knop == 0
                                        screen.blit(kruis,(150, 260))
                                        speler3knop == 0
                                        screen.blit(kruis,(60, 360))
                                        pc3knop == 0
                                        screen.blit(kruis,(150, 360))
                                        speler4knop == 0
                                        screen.blit(kruis,(60, 460))
                                        pc4knop == 0
                                        screen.blit(kruis,(150, 460))
                                        speler1knop = 0
                                        screen.blit(kruis,(60, 160))
                                    pygame.display.update()
                                if 260 < my < 290 and screenWidth/2 - 410 > mx > screenWidth/2 - 440: #button2speler wordt kleur
                                    if speler1knop + pc1knop == 1:
                                        if pc2knop == 1:
                                            pc2knop = 0
                                            screen.blit(kruis,(150, 260))
                                        if speler2knop == 0:
                                            screen.blit(vink,(60, 260))
                                            speler2knop = 1 
                                        else:
                                            speler3knop == 0
                                            screen.blit(kruis,(60, 360))
                                            pc3knop == 0
                                            screen.blit(kruis,(150, 360))
                                            speler4knop == 0
                                            screen.blit(kruis,(60, 460))
                                            pc4knop == 0
                                            screen.blit(kruis,(150, 460))
                                            speler2knop = 0
                                            screen.blit(kruis,(60, 260))
                                        pygame.display.update()
                                if 360 < my < 390 and screenWidth/2 - 410 > mx > screenWidth/2 - 440: #button3speler wordt kleur
                                    if speler1knop + pc1knop + speler2knop + pc2knop == 2:
                                        if pc3knop == 1:
                                            pc3knop = 0
                                            screen.blit(kruis,(150, 360))
                                        if speler3knop == 0:
                                            screen.blit(vink,(60, 360))
                                            speler3knop = 1 
                                        else:
                                            speler4knop == 0
                                            screen.blit(kruis,(60, 460))
                                            pc4knop == 0
                                            screen.blit(kruis,(150, 460))
                                            speler3knop = 0
                                            screen.blit(kruis,(60, 360))
                                        pygame.display.update()
                                if 460 < my < 490 and screenWidth/2 - 410 > mx > screenWidth/2 - 440: #button4speler wordt kleur
                                    if speler1knop + speler2knop + speler3knop + pc1knop + pc2knop + pc3knop == 3:
                                        if pc4knop == 1:
                                            pc4knop = 0
                                            screen.blit(kruis,(150, 460))
                                        if speler4knop == 0:
                                            screen.blit(vink,(60, 460))
                                            speler4knop = 1 
                                        else:
                                            speler4knop = 0
                                            screen.blit(kruis,(60, 460))
                                        pygame.display.update()
                            
                                #pc buttons veranderen kleur
                                if 160 < my < 190 and screenWidth/2 - 320 > mx > screenWidth/2 - 350: #pc1speler wordt kleur
                                    if speler1knop == 1:
                                        speler1knop = 0
                                        screen.blit(kruis,(60, 160))
                                    if pc1knop == 0:
                                        screen.blit(vink,(150, 160))
                                        pc1knop = 1 
                                    else:
                                        speler2knop == 0
                                        screen.blit(kruis,(60, 260))
                                        pc2knop == 0
                                        screen.blit(kruis,(150, 260))
                                        speler3knop == 0
                                        screen.blit(kruis,(60, 360))
                                        pc3knop == 0
                                        screen.blit(kruis,(150, 360))
                                        speler4knop == 0
                                        screen.blit(kruis,(60, 460))
                                        pc4knop == 0
                                        screen.blit(kruis,(150, 460))
                                        pc1knop = 0
                                        screen.blit(kruis,(150, 160))
                                    pygame.display.update()
                                if 260 < my < 290 and screenWidth/2 - 320 > mx > screenWidth/2 - 350: #pc2speler wordt kleur
                                    if speler1knop + pc1knop == 1:
                                        if speler2knop == 1:
                                            speler2knop = 0
                                            screen.blit(kruis,(60, 260))
                                        if pc2knop == 0:
                                            screen.blit(vink,(150, 260))
                                            pc2knop = 1 
                                        else:
                                            speler3knop == 0
                                            screen.blit(kruis,(60, 360))
                                            pc3knop == 0
                                            screen.blit(kruis,(150, 360))
                                            speler4knop == 0
                                            screen.blit(kruis,(60, 460))
                                            pc4knop == 0
                                            screen.blit(kruis,(150, 460))
                                            pc2knop = 0
                                            screen.blit(kruis,(150, 260))
                                        pygame.display.update()
                                if 360 < my < 390 and screenWidth/2 - 320 > mx > screenWidth/2 - 350: #pc3speler wordt kleur
                                    if speler1knop + pc1knop + speler2knop + pc2knop == 2:
                                        if speler3knop == 1:
                                            speler3knop = 0
                                            screen.blit(kruis,(60, 360))
                                        if pc3knop == 0:
                                            screen.blit(vink,(150, 360))
                                            pc3knop = 1 
                                        else:
                                            speler4knop == 0
                                            screen.blit(kruis,(60, 460))
                                            pc4knop == 0
                                            screen.blit(kruis,(150, 460))
                                            pc3knop = 0
                                            screen.blit(kruis,(150, 360))
                                        pygame.display.update()
                                if 460 < my < 490 and screenWidth/2 - 320 > mx > screenWidth/2 - 350: #pc4speler wordt kleur
                                    if speler1knop + speler2knop + speler3knop + pc1knop + pc2knop + pc3knop == 3:
                                        if speler4knop == 1:
                                            speler4knop = 0
                                            screen.blit(kruis,(60, 460))
                                        if pc4knop == 0:
                                            screen.blit(vink,(150, 460))
                                            pc4knop = 1 
                                        else:
                                            pc4knop = 0
                                            screen.blit(kruis,(150, 460))
                                        pygame.display.update()


                                    
                                if 150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #1e naamvakje
                                    #een while loop voor tekst schrijven
                                    klikbuitenvak1 = False
                                    while not klikbuitenvak1:
                                        clock.tick(30) #essentieel!
                                        events = pygame.event.get()
                                        #op kruisje kunnen klikken
                                        for event in events:
                                            if event.type == pygame.QUIT:
                                                quit()
                                        #text schrijven
                                        bordspel.naam(n1)
                                        pygame.display.update()

                                        #buiten het schrijfvak of op Enter klikken om uit de loop te gaan                                                        
                                        events = pygame.event.get()
                                        for event in events:
                                            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #als enter gedrukt wordt ben je ook uit de loop
                                                mx, my = pygame.mouse.get_pos()
                                                if not (150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200) or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #buiten 1e naamvakje
                                                        n1var = n1.update(events)
                                                        klikbuitenvak1 = True
                                                        print ("Speler 1: " + n1var)
                                                        herinner1 = 1
                                if 250 < my < 300 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #2e naamvakje
                                    #een while loop voor tekst schrijven
                                    klikbuitenvak2 = False
                                    while not klikbuitenvak2:
                                        clock.tick(30) #essentieel!
                                        events = pygame.event.get()
                                        #op kruisje kunnen klikken
                                        for event in events:
                                            if event.type == pygame.QUIT:
                                                quit()
                                        #text schrijven
                                        bordspel.naam(n2)
                                        pygame.display.update()

                                        #buiten het schrijfvak of op Enter klikken om uit de loop te gaan                                                        
                                        events = pygame.event.get()
                                        for event in events:
                                            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #als enter gedrukt wordt ben je ook uit de loop
                                                mx, my = pygame.mouse.get_pos()
                                                if not (150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200) or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #buiten 1e naamvakje
                                                        n2var = n2.update(events)
                                                        klikbuitenvak2 = True
                                                        print ("Speler 2: " + n2var)
                                                        herinner2 = 1
                                if 350 < my < 400 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #3e naamvakje
                                    #een while loop voor tekst schrijven
                                    klikbuitenvak3 = False
                                    while not klikbuitenvak3:
                                        clock.tick(30) #essentieel!
                                        events = pygame.event.get()
                                        #op kruisje kunnen klikken
                                        for event in events:
                                            if event.type == pygame.QUIT:
                                                quit()
                                        #text schrijven
                                        bordspel.naam(n3)
                                        pygame.display.update()

                                        #buiten het schrijfvak of op Enter klikken om uit de loop te gaan                                                        
                                        events = pygame.event.get()
                                        for event in events:
                                            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #als enter gedrukt wordt ben je ook uit de loop
                                                mx, my = pygame.mouse.get_pos()
                                                if not (150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200) or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #buiten 1e naamvakje
                                                        n3var = n3.update(events)
                                                        klikbuitenvak3 = True
                                                        print ("Speler 3: " + n3var)
                                                        herinner3 = 1
                                if 450 < my < 500 and screenWidth/2 + 200 > mx > screenWidth/2 - 200: #4e naamvakje
                                    #een while loop voor tekst schrijven
                                    klikbuitenvak4 = False
                                    while not klikbuitenvak4:
                                        clock.tick(30) #essentieel!
                                        events = pygame.event.get()
                                        #op kruisje kunnen klikken
                                        for event in events:
                                            if event.type == pygame.QUIT:
                                                quit()
                                        #text schrijven
                                        bordspel.naam(n4)
                                        pygame.display.update()

                                        #buiten het schrijfvak of op Enter klikken om uit de loop te gaan                                                        
                                        events = pygame.event.get()
                                        for event in events:
                                            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #als enter gedrukt wordt ben je ook uit de loop
                                                mx, my = pygame.mouse.get_pos()
                                                if not (150 < my < 200 and screenWidth/2 + 200 > mx > screenWidth/2 - 200) or pygame.key.get_pressed()[pygame.K_RETURN] == 1: #buiten 1e naamvakje
                                                        n4var = n4.update(events)
                                                        klikbuitenvak4 = True
                                                        print ("Speler 4: " + n4var)
                                                        herinner4 = 1

                        if event.type == pygame.QUIT:
                            quit() 
                            #('subdone' en 'done' True geven om beiden loops af te sluiten kan ook)
                            
            if 350 < my < 400 and screenWidth/2 + 200 > mx > screenWidth/2 - 200:  #'exit'
                quit()
            
            
    
# Be IDLE friendly
pygame.quit()
quit()