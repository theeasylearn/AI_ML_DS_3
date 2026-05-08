import pygame, threading
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
# Optional: pre_init for even better reliability
# pygame.mixer.pre_init(44100, -16, 2, 512)
# pygame.init()  # Only if using full pygame (not needed for mixer)
def play_background(path):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        print(f"Playing: {path}")

        # Wait until done (low CPU)
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)
        print("Playback finished.")
    except Exception as e:
        print(f"Error during playback: {e}")

# play_background('files/sound.mp3')
thread = threading.Thread(target=play_background, args=("files/sound.mp3",), daemon=True)
thread.start()
print("Sound is playing in background...")
thread.join()  # This waits for play_background() to complete