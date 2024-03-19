import pygame

pygame.init()

white = 255, 255, 255
red = 255, 0, 0
size = width, height = 1200, 600

running =True
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Ball")

position = pygame.Vector2(width/2, height/2)
dt=0

while running:
    screen.fill(white)
    pygame.draw.circle(screen, red, position, 25)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if position.y>0+25:
        if keys[pygame.K_w]:
            position.y -= 20
    if position.y<height-25:
        if keys[pygame.K_s]:
            position.y += 20
    if position.x>0+25:
        if keys[pygame.K_a]:
            position.x -= 20
    if position.x<width-25:
        if keys[pygame.K_d]:
            position.x += 20
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()