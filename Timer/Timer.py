import pygame
pygame.init()
screen = pygame.display.set_mode((218, 128))
clock = pygame.time.Clock()

counter, text = 50, '50'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Too Slow!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((0, 0, 0))
        screen.blit(font.render(text, True, (255, 255, 255)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
