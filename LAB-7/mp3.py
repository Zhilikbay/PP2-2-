import pygame, sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Verdana", 20)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")


music_playlist = ["\AZ\PP2(2)\LAB-7\sounds\sample1.mp3", "\AZ\PP2(2)\LAB-7\sounds\sample2.mp3", "\AZ\PP2(2)\LAB-7\sounds\sample3.mp3"]
current_song = 0
paused = False

pygame.mixer.init()


pygame.mixer.music.load(music_playlist[current_song])

key_mapping = {
    pygame.K_UP: "play_pause",
    pygame.K_DOWN: "stop",
    pygame.K_RIGHT: "next",
    pygame.K_LEFT: "previous"
}

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key in key_mapping:
                action = key_mapping[key]
                if action == "play_pause":
                    if pygame.mixer.music.get_busy():
                        if paused:
                            pygame.mixer.music.unpause()
                            paused = False
                        else:
                            pygame.mixer.music.pause()
                            paused = True
                    else:
                        pygame.mixer.music.play()
                        paused = False
                elif action == "stop":
                    pygame.mixer.music.stop()
                    paused = False
                elif action == "next":
                    current_song = (current_song + 1) % len(music_playlist)
                    pygame.mixer.music.load(music_playlist[current_song])
                    pygame.mixer.music.play()
                    paused = False
                elif action == "previous":
                    current_song = (current_song - 1) % len(music_playlist)
                    pygame.mixer.music.load(music_playlist[current_song])
                    pygame.mixer.music.play()
                    paused = False

    screen.fill(WHITE)

    current_song_text = font.render("Current Song: {}".format(music_playlist[current_song]), True, BLACK)
    screen.blit(current_song_text, (10, 10))

    play_pause_text = font.render("Paused" if paused else "Playing", True, BLACK)
    screen.blit(play_pause_text, (10, 40))


    instructions_text = font.render("Press 'Up' to Play/Pause, 'Down' to Stop, 'Right' for Next, 'Left' for Previous", True, BLACK)
    screen.blit(instructions_text, (10, 70))

    
    pygame.display.update()