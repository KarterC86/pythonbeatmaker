import pygame
from pygame import mixer
pygame.init()
width = 1400
height = 800

black = (0, 0, 0)
white = (255, 255, 255)
gay = (128, 128, 128)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("sick beats")
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
beats = 8
instruments = 6
timer= pygame.time.Clock()



def draw_grid():
    left_box = pygame.draw.rect(screen, gay, [0, 0, 200, height], 5)
    bottome_box = pygame.draw.rect(screen, gay, [0, height -200, width, 200], 5)
    boxes = []
    colors = {gay, white, gay}

    hi_hat_text = label_font.render('hi hat', True, white)
    screen.blit(hi_hat_text, (30, 30))

    snare_text = label_font.render('snare', True, white)
    screen.blit(snare_text, (30, 130))

    kick_text = label_font.render('base', True, white)
    screen.blit(kick_text, (30, 230))

    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330)) 

    kick_text = label_font.render('Clap', True, white)
    screen.blit(kick_text, (30, 430))

    crash_text = label_font.render('Floor Tom', True, white)
    screen.blit(crash_text, (30, 530)) 
    for i in range(6):
        pygame.draw.line(screen, white, (0, (i * 100) + 100), (200, (i * 100)+ 100), 5)

    #this is for the beats 
    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gay, [i * ((width - 200) // beats) + 200, (j * 100), ((width - 200) // beats), ((height - 200) // instruments)], 5, 5)
run = True
while run: 
    timer.tick(fps) 
    screen.fill (black)

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
             
    pygame.display.flip()
pygame.quit() 
#the closing of the game 
 

