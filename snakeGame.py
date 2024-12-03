import pygame
import random
pygame.init()
W = 700
H = 500
screen = pygame.display.set_mode((W,H)) 
white = 255,255,255
red = 255,0,0
x,y,w,h = 200,200,25,25
move_x,move_y=0,0
green = 0,255,0
en_x,en_y,en_w,en_h = 100,100,25,25
counter = 0
black = 0,0,0
# AUDIO
hitSound = pygame.mixer.Sound("doorHit.mp3")
def Score(counter):
    # font define - size , type
    font = pygame.font.SysFont(None,30)
    # text,antialias,color
    text =  font.render(f"Score : {counter}",True,black)
    # blit - print
    screen.blit(text,(10,10))
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                move_y=-0.5
                move_x=0
            elif event.key==pygame.K_DOWN:
                move_y=0.5
                move_x=0
            elif event.key==pygame.K_LEFT:
                move_y=0
                move_x = -0.5
            elif event.key==pygame.K_RIGHT:
                move_y=0
                move_x=0.5
    snake = pygame.draw.rect(screen,red,[x,y,w,h])
    enemy = pygame.draw.rect(screen,green,[en_x,en_y,en_w,en_h])
    x+=move_x
    y+=move_y
    Score(counter)
    if snake.colliderect(enemy):
        en_x = random.randint(0,W-en_w)
        en_y = random.randint(0,H-en_h)
        counter+=1
        hitSound.play()

    if x<0:
        x = W-w
    elif x>W-w:
        x=0

    elif y<0:
        y = H-h
    elif y>H-h:
        y=0
        
    pygame.display.update()
