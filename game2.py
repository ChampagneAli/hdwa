from pygame.locals import *
import pygame, string, random, psycopg2
from test import *
from math import pi
pygame.init()

# Background image is set as 'bg'
bg = pygame.image.load("FOTO achtergrond.png")
vink = pygame.image.load("FOTO groen vinkje.png")
kruis = pygame.image.load("FOTO rood kruisje.png")
arrow = pygame.image.load("FOTO arrow.png")
speelbord_bg = pygame.image.load("FOTO speelbord.png")
correct = pygame.image.load("FOTO correct.png")
correct_verder = pygame.image.load("FOTO correct_verder.png")
incorrect = pygame.image.load("FOTO incorrect.png")
page1 = pygame.image.load("page1.jpg")

page2 = pygame.image.load("page2.jpg")
page3 = pygame.image.load("page3.jpg")
page4 = pygame.image.load("page4.jpg")

#sounds
#pygame.mixer.music.load('got.mp3')

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

#database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=pr2 user=Ali password=0000")
    cursor = connection.cursor()
    
    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        #Nothing to fetch
        pass

    print(results)
    # Close connection
    cursor.close()
    connection.close()
    
    return results


    # Uploads a score into the hiscore table
    #def upload_score(name, score):
    #    interact_with_database("UPDATE score SET score = score WHERE name = name".format(score, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM test")


# Downloads the top score from database
#def download_top_score():
    #  result = interact_with_database("SELECT * FROM score ORDER BY highscore")[0][1]
    #  return result
#upload_score(str(input("Score: ")), str(input("Name: ")))
#print (results)


#alle vragen
#entertainment categorie

"""
Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd?
    A. De Witte Aap
    B. Het NRC
    C. Caf� de Beurs

Hoe heet de bekendste escape room in Rotterdam?
	A. R�dam Escape
	B. Escape010
	C. Room Escape
Voor welk vervoermiddel is er geen tour door Rotterdam beschikbaar?
	A. Segway
	B. Boot
	C. Auto
Welk van de volgende winkels is niet rond de koopgoot?
	A. H&M
	B. Media Markt
	C. The Sting
In welke bioscoop vindt het Wildlife Film Festival plaats?
	A. Cinerama
	B. Path� de Kuip
	C. Path� Schouwburgplein
Voor welk museum staat het monument van Zadkine genaamd �De Verwoest Stad�?
	A. Havenmuseum
	B. Mariniersmuseum
	C. Maritiem museum
Waar geeft de Rotterdam Tours onder andere rondleidingen?
	A. De Euromast
	B. Museumplein
	C. De Markthal
Welke van de volgende Path� bioscopen is niet in Rotterdam?
	A. Path� de Kuip
	B. Path� de Kroon
	C. Path� Schouwburgplein
Hoeveel bezoekers zijn er jaarlijks bij de Marathon Rotterdam?
	A. 925.000 bezoekers
	B. 675.000 bezoekers
	C. 830.000 bezoekers
Waar kan je niet terecht om te gaan zwemmen?
	A. Hoek van Holland
	B. Euromast Park 
	C. Plaswijckpark
Welke landen kun je behalve Nederland ook in Miniworld Rotterdam zien?
	A. Luxemburg en Belgi�
	B. Duitsland en Belgi�
	C. Duitsland en Frankrijk
Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?
	A. Drive & Eat
	B. Bicycle Diner
	C. Bike & Bite
Welk van de volgende restaurantboten in Rotterdam bestaat niet?
	A. De Zwanenboot
	B. De Pannenkoekenboot
	C. De Berenboot
"""
#geografie
"""
Welke brug in Rotterdam heeft de volgende bijnaam: De zwaan.
A.	De Willemsbrug
B.	De Erasmusbrug
C.	De van Briennenoordbrug
Rotterdam is de hoofdstad van Nederland. 
A.	 Waar
B.	 Niet Waar
Rotterdam is de hoofdstad van Zuid-Holland.
A.	 Waar
B.	 Niet Waar
Rotterdam is de grootste stad van Nederland.
A.	 Waar
B.	 Niet Waar
De haven van Rotterdam is de grootste haven van Nederland.
A.	 Waar
B.	 Niet Waar
Wat is het belangrijkste vervoersmiddel in Rotterdam?
A.	 Metro
B.	 Auto
C.	 Fiets
Hoeveel millimeter regen valt er gemiddeld per jaar in Rotterdam?
A.	 760 tot 780mm
B.	 780 tot 800mm
C.	 800 tot 820mm
Hoeveel woningen zijn er ongeveer in Rotterdam?
A.	 150.000
B.	 300.000
C.	 450.000
Wat is het oudste gebouw van Rotterdam?
A.	 Kerktoren hillegondakerk
B.	 St. Laurenskerk.
C.	 Stadhuis van Rotterdam
Hoeveel mensen maken dagelijks gebruik van het openbaar vervoer in Rotterdam?
A.	 800.000	
B.	 900.000	
C.	 1.000.000
Wat is de oudste brug van Rotterdam?
A.	 De Willemsbrug
B.	 De Koninginnebrug
C.	 De van Briennenoordbrug
Rotterdam word ook wel de �. Genoemd
A.	 stad der wonderen
B.	 stad der steden
C.	 Haven stad
In welke provincie ligt Rotterdam?
A.	 Noord-Holland
B.	 Zuid-Holland
C.	 Noord-Brabant
Hoe heet de grootste rivier waar Rotterdam aan grenst?
A.	 De Maas
B.	 De Rijn
C.	 De Waal
"""
#historie
"""
Waar dankt Rotterdam zijn naam aan?
A.	Kooplieden hadden dit vroeger bedacht 
B.	Aan de rivier de rotte
C.	Er was een dam aangelegd in de maas
Wat is het enigste overgebleven middeleeuws gebouw in de binnenstad van Rotterdam?
A.	De oude haven
B.	VOC magazijn
C.	St. Laurenskerk
Wie is de nachtburgemeester van Rotterdam?
A.	Ahmed Aboutaleb 
B.	Jules Deelder
C.	Willem Alexander
Was de eerste metrolijn in Nederland in Rotterdam geopend?
A.	Waar, in 1968 
B.	Niet waar 
Wanneer is diergaarde Blijdorp geopend?
A.	1855
B.	1975
C.	1915
Welk gebouw (gebouwd in 1957) stond symbool voor de wederopbouw van de stad?
A.	De Bijenkorf
B.	De Kubuswoningen
C.	The red apple
Wat is de offici�le naam van de koopgoot?
A.	De ondergrondse winkelstraat
B.	Beurstraverse
C.	Gewoon de koopgoot
In welk jaar heeft Rotterdam stadsrechten gekregen?
A.	1250
B.	1340 
C.	1590
Door welke architect(en) is de Euromast ontworpen?
A.	Maaskant
B.	Brinkman en van der Vlugt
C.	c. Koolhaas 
Hoe heette de haven van Rotterdam oorspronkelijk tijdens zijn ontstaan?
A.	Waalhaven
B.	De Maashaven
C.	Europoort
Rotterdam was tot 1870 een opslag haven, welke producten werden er onder ander opgeslagen?
A.	Suiker
B.	Wol
C.	Cacao
"""
#sport
"""
In welk jaar startte de Tour de France in Rotterdam?
A.	2000
B.	2005
C.	2010
Welk tennistoernooi word er elk jaar in Ahoy gehouden?
A.	ABN AMRO World Tennis Tournament
B.	Ahoy Open
C.	Heineken Open
Wat is een hockeyclub uit Rotterdam?
A.	HVGR
B.	Focus
C.	HC Rotterdam
Welke manier van sport word het meest beoefend in Rotterdam?
A.	Fitness
B.	Voetbal
C.	Basketbal
Welke Olympi�r groeide op in Rotterdam? 
A.	Dorian van Rijsselberghe
B.	Marhinde Verkerk
C.	Edith Bosch
Op welke baan vond het WK roeien in 2016 plaats?
A.	Willem Alexander baan
B.	Beatrix baan
C.	Juliana baan
Op welke positie in het veld speelde Coen Moulijn voor zowel Feyenoord als het Nederlands elftal? 
A.	Rechtsback
B.	Linksback
C.	LinksbuitenHoeveel spelers staan er per team bij lacrosse op het veld?
A.	9
B.	10
C.	11
Hoe heet het stadion van Sparta Rotterdam?
A.	De Toren
B.	Het Kasteel
C.	De Arena
Hoe lang is de NN Marathon van Rotterdam?
A.	42,125 km
B.	42,450 km
C.	42,680 km
Een honkbal is groter dan een softbal. 
A.	Waar
B.	Niet Waar
C.	Even groot
Hoeveel mensen staan er achter de slagman bij honkbal?
A.	1
B.	2
C.	3
In welk jaar is de honkbalclub Neptunes opgericht?
A.	1850
B.	1875 
C.	1900 
"""


#\simpele manier voor random getal ipv dice
"""import random
def rollDice():
    roll=int(random.randint(1,6))
    return roll
"""


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
n1 = Input(maxlength=15, color=(0,0,0), prompt='typ: ')
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
 
#fonts and texts
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
#vragen
text22 = fontsmall.render('Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd?', True, BLACK)
text22_a = fontsmall.render('A. De Witte Aap', True, BLACK)
text22_b = fontsmall.render('| B. Het NRC', True, BLACK)
text22_c = fontsmall.render('| C. Cafe de Beurs', True, BLACK)
text23 = fontsmall.render('Hoe heet de bekendste escape room in Rotterdam?', True, BLACK)
text23_a = fontsmall.render("A. R'dam Escape", True, BLACK)
text23_b = fontsmall.render('| B. Escape010', True, BLACK)
text23_c = fontsmall.render('| C. Room Escape', True, BLACK)
text24 = fontsmall.render('Voor welk vervoermiddel is er geen tour door Rotterdam beschikbaar?', True, BLACK)
text24_a = fontsmall.render('A. Segway', True, BLACK)
text24_b = fontsmall.render('| B. Boot', True, BLACK)
text24_c = fontsmall.render('| C. Auto', True, BLACK)
text25 = fontsmall.render('Welk van de volgende winkels is niet rond de koopgoot?', True, BLACK)
text25_a = fontsmall.render('A. H&M', True, BLACK)
text25_b = fontsmall.render('| B. Media Markt', True, BLACK)
text25_c = fontsmall.render('| C. The Sting', True, BLACK)
text26 = fontsmall.render('In welke bioscoop vindt het Wildlife Film Festival plaats?', True, BLACK)
text26_a = fontsmall.render('A. Cinerama', True, BLACK)
text26_b = fontsmall.render('| B. Pathe de Kuip', True, BLACK)
text26_c = fontsmall.render('| C. Pathe Schouwburgplein', True, BLACK)
text27 = fontsmall.render("Voor welk museum staat het monument van Zadkine genaamd 'De Verwoeste Stad'?", True, BLACK)
text27_a = fontsmall.render('A. Havenmuseum', True, BLACK)
text27_b = fontsmall.render('| B. Mariniersmuseum', True, BLACK)
text27_c = fontsmall.render('| C. Maritiem museum', True, BLACK)
text28 = fontsmall.render('Waar geeft de Rotterdam Tours onder andere rondleidingen?', True, BLACK)
text28_a = fontsmall.render('A. De Euromast', True, BLACK)
text28_b = fontsmall.render('| B. Museumplein', True, BLACK)
text28_c = fontsmall.render('| C. De Markthal', True, BLACK)
text29 = fontsmall.render('Welke van de volgende Path� bioscopen is niet in Rotterdam?', True, BLACK)
text29_a = fontsmall.render('A. Pathe de Kuip', True, BLACK)
text29_b = fontsmall.render('| B. Pathe de Kroon', True, BLACK)
text29_c = fontsmall.render('| C. Pathe Schouwburgplein', True, BLACK)
text30 = fontsmall.render('Hoeveel bezoekers zijn er jaarlijks bij de Marathon Rotterdam?', True, BLACK)
text30_a = fontsmall.render('A. 925.000 bezoekers', True, BLACK)
text30_b = fontsmall.render('| B. 675.000 bezoekers', True, BLACK)
text30_c = fontsmall.render('| C. 830.000 bezoekers', True, BLACK)
text31 = fontsmall.render('Waar kan je niet terecht om te gaan zwemmen?', True, BLACK)
text31_a = fontsmall.render('A. Hoek van Holland', True, BLACK)
text31_b = fontsmall.render('| B. Euromast Park', True, BLACK)
text31_c = fontsmall.render('| C. Plaswijckpark', True, BLACK)
#text13-16 zijn bezet
#20 21 42 43 zijn bezet
text100 = font.render("Highscore", True, WHITE)
text100a = fontsmall.render('Speler Highscores', True, WHITE)
text100b = fontsmall.render('Loading Scores From Database', True, WHITE)
text101 = font.render("Handleiding", True, WHITE)
text108 = font.render("Next", True, WHITE)
#begin values voor de start error
error10 = 0 
error11 = 0


                                                                      #DEFINED SCREENS AND FUNCTIONS

class bordspel: 
    def vraag(ant_a, ant_b, ant_c):
        beantwoord = False
        while not beantwoord:
            goed = 0
            mx, my = pygame.mouse.get_pos()
            if 195 < my < 235 and 5 < mx < 238: #antwoord a
                if ant_a == 1:
                    screen.blit(correct,(0,0))
                    goed = 1
                if ant_a == 0:
                    screen.blit(incorrect,(0,0))
                beantwoord = True
            if 195 < my < 235 and 238 < mx < 472: #antwoord b
                if ant_b == 1:
                    screen.blit(correct,(0,0))
                    goed = 1
                if ant_b == 0:
                    screen.blit(incorrect,(0,0))
                beantwoord = True
            if 195 < my < 235 and 472 < mx < 705: #antwoord c
                if ant_c == 1:
                    screen.blit(correct,(0,0))
                    goed = 1
                if ant_c == 0:
                    screen.blit(incorrect,(0,0))
                beantwoord = True
            pygame.display.update()
            return(goed)

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
        if my > 450 and my < 500 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 450, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 450, 400, 50])
        if my > 550 and my < 600 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
            pygame.draw.rect(screen, GREY, [screenWidth/2 - 200, 550, 400, 50])
        else:
            pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 550, 400, 50])
        pygame.display.set_caption("The Euromast")
        screen.blit(text, [screenWidth/2 - 30, 157])
        screen.blit(text2, [screenWidth/2- 85, 257])
        screen.blit(text3, [screenWidth/2 - 25, 557])
        screen.blit(text9, [300, 20])
        screen.blit(text100, [screenWidth/2 - 55 , 457])
        screen.blit(text101, [screenWidth/2 - 68, 357])
        #geef error als op start geklikt word
        if error10 == 1:
            screen.blit(text10, [15, 95]) #start-error
            screen.blit(arrow,(0,0))
        if error11 == 1:
            screen.blit(text11, [20, 100]) #start-error
            screen.blit(arrow,(0,0))

    def handleiding():
        

        #terug knop
        pygame.draw.rect(screen, BLUE, [screenWidth/2 - 440, 530, 90, 40])
        screen.blit(text7, [screenWidth/2 - 430, 530, 90, 800]) 
        #next knop
        pygame.draw.rect(screen, BLUE, [800, 530, 90, 40])
        screen.blit(text108, [816, 532, 90, 800]) 
        
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

    def highscore():
        screen.blit(bg,(0,0))
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, LIGHT_BLUE, [screenWidth/2 - 200, 70, 400, 50]) 
        screen.blit(text100a, [screenWidth/2 - 75, 80])
        pygame.draw.rect(screen, BLACK, [screenWidth/2 - 200, 150, 400, 400]) 
        screen.blit(text100b, [screenWidth/2 - 110, 170])

    def spel():
        #pygame.mixer.music.play(-1)
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
        text20 = font.render('Dobbelsteen = 1: ' + n1var, True, RED)
        text21 = font.render( 'Dobbelsteen = 2: ' + n2var, True, BLUE)
        text42 = font.render( 'Dobbelsteen = 3: ' + n3var, True, GREEN)
        text43 = font.render('Dobbelsteen = 4: ' + n4var, True, WHITE)
        pygame.draw.rect(screen, GREY, [5, 120, 700, 150])
        pygame.draw.rect(screen, WHITE, [5, 195, 700, 40])
        pygame.display.update()
        aantal = speler1knop + speler2knop + speler3knop + speler4knop + pc1knop + pc2knop + pc3knop + pc4knop #begin beurt
        randomdobbel = int(random.randint(1,aantal))
        vraagrandom = int(random.randint(1,10))
        print('vraagrandom: ' + str(vraagrandom))
        if randomdobbel == 1: #eerste speler is random gekozen
            screen.blit(text20,[10,120])
        elif randomdobbel == 2: #tweede speler is random gekozen 
            screen.blit(text21,[10,120])
        elif randomdobbel == 3: #derde speler is random gekozen
            screen.blit(text42,[10,120])
        elif randomdobbel == 4: #vierde speler is random gekozen
            screen.blit(text43,[10,120])
        if vraagrandom == 1:            #vragen
            screen.blit(text22,[10,150])
            screen.blit(text22_a,[10,200])
            screen.blit(text22_b,[238,200])
            screen.blit(text22_c,[477,200])
        if vraagrandom == 2:
            screen.blit(text23,[10,150])
            screen.blit(text23_a,[10,200])
            screen.blit(text23_b,[238,200])
            screen.blit(text23_c,[477,200])
        if vraagrandom == 3:
            screen.blit(text24,[10,150])
            screen.blit(text24_a,[10,200])
            screen.blit(text24_b,[238,200])
            screen.blit(text24_c,[477,200])
        if vraagrandom == 4:
            screen.blit(text25,[10,150])
            screen.blit(text25_a,[10,200])
            screen.blit(text25_b,[238,200])
            screen.blit(text25_c,[477,200])
        if vraagrandom == 5:
            screen.blit(text26,[10,150])
            screen.blit(text26_a,[10,200])
            screen.blit(text26_b,[238,200])
            screen.blit(text26_c,[477,200])
        if vraagrandom == 6:
            screen.blit(text27,[10,150])
            screen.blit(text27_a,[10,200])
            screen.blit(text27_b,[238,200])
            screen.blit(text27_c,[477,200])
        if vraagrandom == 7:
            screen.blit(text28,[10,150])
            screen.blit(text28_a,[10,200])
            screen.blit(text28_b,[238,200])
            screen.blit(text28_c,[477,200])
        if vraagrandom == 8:
            screen.blit(text29,[10,150])
            screen.blit(text29_a,[10,200])
            screen.blit(text29_b,[238,200])
            screen.blit(text29_c,[477,200])
        if vraagrandom == 9:
            screen.blit(text30,[10,150])
            screen.blit(text30_a,[10,200])
            screen.blit(text30_b,[238,200])
            screen.blit(text30_c,[477,200])
        if vraagrandom == 10:
            screen.blit(text31,[10,150])
            screen.blit(text31_a,[10,200])
            screen.blit(text31_b,[238,200])
            screen.blit(text31_c,[477,200])
        pygame.display.update()
        return vraagrandom


counter = 1

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

            if my > 550 and my < 600 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:
                screen.blit(page1,(0,0))

            if 350 < my < 400 and screenWidth/2 + 200 > mx > screenWidth/2 - 200:
                screen.blit(page1,(0,0))
                bordspel.handleiding()
                pygame.display.update()
                sub2done = False
                while not sub2done:
                    for event in pygame.event.get(): # User input kan worden opgehaald -> print(event)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1: # 1links 2midden 3rechts 4scrollup 5scrolldown
                                mx, my = pygame.mouse.get_pos()
                                if 530 < my < 570 and 800 < mx < 890: #next
                                    print(counter)
                                    counter = counter + 1
                                    if counter == 2:
                                        screen.blit(page2,(0,0))
                                        bordspel.handleiding()
                                    if counter == 3:
                                        screen.blit(page3,(0,0))
                                        bordspel.handleiding()
                                    if counter == 4:
                                        screen.blit(page4,(0,0))
                                        bordspel.handleiding()
                                    if counter == 5:
                                        screen.blit(page1,(0,0))
                                        counter = 1
                                        bordspel.handleiding()
                                    pygame.display.update()
                                if 530 < my < 570 and screenWidth/2 - 350 > mx > screenWidth/2 - 440: #terug'
                                    bordspel.start() 
                                    pygame.draw.rect(screen, BLUE, [screenWidth/2 - 440, 530, 90, 40])               
                                    pygame.display.update()
                                    sub2done = True
                                              
                        if event.type == pygame.QUIT:
                            quit()
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
                    spelvoorbij = False
                    while not spelvoorbij: #spelvoorbij gewoon ff false houden
                        beurtvoorbij = False
                        while not beurtvoorbij:
                            vraagrandom = bordspel.spel()
                            pygame.display.update()
                            beantwoord = False
                            while not beantwoord:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mx, my = pygame.mouse.get_pos()
                                        if 195 < my < 235 and 5 < mx < 705:
                                            if vraagrandom == 1 or vraagrandom == 5 or vraagrandom == 9:
                                                goed = bordspel.vraag(1,0,0)
                                                beantwoord = True
                                            if vraagrandom == 2 or vraagrandom == 4 or vraagrandom == 8 or vraagrandom == 10:
                                                goed = bordspel.vraag(0,1,0)
                                                beantwoord = True
                                            if vraagrandom == 3 or vraagrandom == 6 or vraagrandom == 7:
                                                goed = bordspel.vraag(0,0,1)
                                                beantwoord = True
                                            
                                            if goed == 1:
                                                pijltje = False
                                                while not pijltje:
                                                    for event in pygame.event.get():
                                                        if event.type == KEYUP or event.type == MOUSEBUTTONDOWN:
                                                            mx, my = pygame.mouse.get_pos()
                                                            if 515 < my < 578 and 475 < mx < 544 or event.type == KEYUP:
                                                                #poppetje omhoog laten klimmen
                                                                screen.blit(correct_verder,(0,0))
                                                                pijltje = True
                                                            
                                                        if event.type == K_LEFT or event.type == MOUSEBUTTONDOWN:
                                                            mx, my = pygame.mouse.get_pos()
                                                            if 515 < my < 578 and 400 < mx < 470 or event.type == K_LEFT:
                                                                #poppetje omhoog en links laten klimmen
                                                                screen.blit(correct_verder,(0,0))
                                                                pijltje = True

                                                        if event.type == K_RIGHT or event.type == MOUSEBUTTONDOWN:
                                                            mx, my = pygame.mouse.get_pos()
                                                            if 515 < my < 578 and 550 < mx < 618 or event.type == K_RIGHT:
                                                                #poppetje omhoog en rechts laten klimmen
                                                                screen.blit(correct_verder,(0,0))
                                                                pijltje = True
                                                        pygame.display.update()
                                                        if event.type == pygame.QUIT:
                                                            quit()

                                            verdergeklikt = False
                                            while not verdergeklikt:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mx, my = pygame.mouse.get_pos()
                                                        if 507 < my < 555 and 55 < mx < 192:
                                                            verdergeklikt = True
                                                            beurtvoorbij = True
                                                    if event.type == pygame.QUIT:
                                                        quit()

                                            
                                    if event.type == pygame.QUIT:
                                        quit()
                            
                    done = False
                    while not done:
                        for event in pygame.event.get(): # User input kan worden opgehaald -> print(event)
                            if event.type == pygame.QUIT:
                                done = True
            if left_mouse == 1:
                mx, my = pygame.mouse.get_pos()
                if 450 < my < 500 and screenWidth/2 + 500 > mx > screenWidth/2 - 500: #'highscore'
                    bordspel.highscore()
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
                                        clock.tick(10) #essentieel!
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
                                        clock.tick(10) #essentieel!
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
                                        clock.tick(10) #essentieel!
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
                                        clock.tick(10) #essentieel!
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
                            
            if my > 550 and my < 600 and mx < screenWidth/2 + 200 and mx > screenWidth/2 - 200:  #'exit'
                pygame.quit()
                quit()
            
            
    
# Be IDLE friendly
pygame.quit()
quit()