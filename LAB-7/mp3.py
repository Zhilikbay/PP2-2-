import pygame, sys

# Initialize pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.SysFont("Verdana", 20)

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

# Set up music playlist
music_playlist = ["\AZ\PP2(2)\LAB-7\sounds\sample1.mp3", "\AZ\PP2(2)\LAB-7\sounds\sample2.mp3", "\AZ\PP2(2)\LAB-7\sounds\sample3.mp3"]
current_song = 0
paused = False

# Initialize music player
pygame.mixer.init()

# Load initial song
pygame.mixer.music.load(music_playlist[current_song])

# Keyboard mapping for music player actions
key_mapping = {
    pygame.K_p: "play_pause",
    pygame.K_s: "stop",
    pygame.K_n: "next",
    pygame.K_b: "previous"
}

# Main game loop
while True:
    # Handle events
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

    # Clear the screen
    screen.fill(WHITE)

    # Display current playing song
    current_song_text = font.render("Current Song: {}".format(music_playlist[current_song]), True, BLACK)
    screen.blit(current_song_text, (10, 10))

    # Display play/pause status
    play_pause_text = font.render("Paused" if paused else "Playing", True, BLACK)
    screen.blit(play_pause_text, (10, 40))

    # Display instructions
    instructions_text = font.render("Press 'P' to Play/Pause, 'S' to Stop, 'N' for Next, 'B' for Previous", True, BLACK)
    screen.blit(instructions_text, (10, 70))

    # Update the screen
    pygame.display.update()