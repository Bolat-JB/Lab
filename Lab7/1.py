import pygame, sys, datetime
pygame.init()

Gray = 0, 0, 45
size = width, height = 900, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clock")

clock = pygame.image.load("main-clock.png")
mhand = pygame.image.load("right-hand.png")
shand = pygame.image.load("left-hand.png")
clockrect = clock.get_rect()

clockrect.center = (width//2, height//2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    now = datetime.datetime.now()
    microsec = now.microsecond
    sec = now.second
    min = now.minute
    rotate_sec = 88 - sec*6 - (microsec/999999)*6
    rotate_min = 85 - min*6 - (sec/60)*6 
    
    min_hand = pygame.transform.rotate(mhand, rotate_min)
    sec_hand = pygame.transform.rotate(shand, rotate_sec)
    mhandrect = min_hand.get_rect()
    shandrect = sec_hand.get_rect()
    mhandrect.center = (width//2, height//2)
    shandrect.center = (width//2, height//2)
    
    
    screen.fill(Gray)
    screen.blit(clock, clockrect)
    screen.blit(min_hand, mhandrect)
    screen.blit(sec_hand, shandrect)
    pygame.display.flip()


