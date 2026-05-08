# write a program that will fetch Rashi bhavishya from internet and play it as audio using text to speech module 
#task to do (play rashi bhavishya as per user given birth date  (decide zodiac sign ))
'''
    1) fetch today Rashi bhavishya in gujarati from given url
    2) play text text using text to speech module 
'''
from bs4 import BeautifulSoup
import requests
import os
import tempfile
import threading
#download module
import pygame
from gtts import gTTS

# Initialize pygame mixer in main thread (MUST be before any thread)
pygame.mixer.pre_init(44100, -16, 2, 512)  # Best settings
pygame.mixer.init()

def get_rashi_bhavishya(webpage):
        html = requests.get(webpage)
        soup = BeautifulSoup(html.text, 'html.parser')
        mytext = soup.find('div',class_='a6b3d8fe')
        bhavishya = '' #string
        for item in mytext.find_all('p'):
            bhavishya = bhavishya + item.text
        # print('_'*100)

        return bhavishya
def speak(text: str, lang: str = 'gu', slow: bool = False):
    """
    Convert text to speech and play in background using pygame.
    Supports Gujarati, Hindi, Tamil, etc. No window opens.
    """
    # Skip empty text
    if not text.strip():
        print("Empty text. Skipping speech.")
        return

    # Create temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3').name

    def generate_and_play():
        try:
            # Generate TTS
            print(f"Generating speech in {lang}...")
            tts = gTTS(text=text, lang=lang, slow=slow)
            tts.save(temp_file)

            # Play with pygame
            print(f"Playing audio: {len(text)} characters")
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()

            # Wait until playback ends (low CPU)
            clock = pygame.time.Clock()
            while pygame.mixer.music.get_busy():
                clock.tick(10)

            print("Playback finished.")

        except Exception as e:
            print(f"Error in TTS/playback: {e}")
        finally:
            # Always clean up
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except:
                pass

    # Run in background thread
    thread = threading.Thread(target=generate_and_play, daemon=True)
    thread.start()
    return thread  # Return thread so caller can .join() if needed

rashi = 13
webpage = f"https://www.divyabhaskar.co.in/rashifal/{rashi}/today?ref=inbound_RHS"
bhavishya = get_rashi_bhavishya(webpage)
audio_thread = speak(bhavishya, lang='gu', slow=False)
# Wait for audio to finish (CRITICAL!)
if audio_thread:
    audio_thread.join()  # This keeps main thread alive
print("Horoscope playback completed. Good bye!")