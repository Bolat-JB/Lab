import pygame, os, re

pygame.init()

def theme():

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(120, 50, 400, 40))
    
    font = pygame.font.SysFont('arial', 20)
    manual = "SPACE to start and pause_press  '->' next song_<-' previous song"
    point = 280
    for i in manual.split('_'):
        m = font.render(i, True, (255, 255, 255))
        if 'press' in i or 'SPACE' in i: screen.blit(m, (150, point))
        else: screen.blit(m, (150, point))
        point += 20

def get_path(path):
    canon_path = path.replace('/',os.sep).replace('\\',os.sep)
    return canon_path

def track_name(playlist, track, screen):
    font = pygame.font.SysFont('arial', 25)
    track_name = playlist[track]
    track_name = re.sub('.ogg', '', track_name)
    track_name = re.sub('.mp3', '', track_name) 
    screen.blit(font.render(track_name, True, (255, 255, 255)), (120, 50))

def next_song(track, playlist, state):
    if state:
        if track != len(playlist) - 1: track += 1
        else: track = 0
    else:
        if track != 0: track -= 1 
        else: track = len(playlist) - 1
    return track

def load_new_song(track, playlist):
    pygame.mixer.music.load(get_path(f'mus/{playlist[track]}'))
    pygame.mixer.music.play(0)


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Music Player')
playlist = [i for i in os.listdir('mus') if '.ogg' in i or '.mp3' in i]
track = 0

run = True 
play = False

while run:
    theme()
    track_name(playlist, track, screen)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN: 
            if i.key == pygame.K_SPACE:
                if not play: 
                    load_new_song(track, playlist)
                else: pygame.mixer.music.pause()
                play = not play
            if i.key == pygame.K_RIGHT and play:
                track = next_song(track, playlist, True)
                load_new_song(track, playlist)
            if i.key == pygame.K_LEFT and play:
                track = next_song(track, playlist, False)
                load_new_song(track, playlist)
        if pygame.mixer.music.get_busy() == False and play:
            track = next_song(track, playlist, True)
            load_new_song(track, playlist)
    pygame.display.update()
