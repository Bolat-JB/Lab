import pygame, os

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

music_dir = "D:\KBTU\A_SEM2\PP 2\Lab7"
music_files = [filename for filename in os.listdir(music_dir) if filename.endswith(".mp3")]

current_track = 0
is_playing = False

if music_files:
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()
                is_playing = True
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()
                is_playing = True

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
