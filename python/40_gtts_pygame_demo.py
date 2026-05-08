#built in module
import os
import tempfile
import threading
#download module
import pygame
from gtts import gTTS

# Initialize pygame mixer in main thread (MUST be before any thread)
pygame.mixer.pre_init(44100, -16, 2, 512)  # Best settings
pygame.mixer.init()

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


# ——— MAIN EXAMPLE ———
if __name__ == "__main__":
    horoscope_text = """
પોઝિટિવ: છેલ્લા કેટલાક સમયથી ચાલી રહેલી સમસ્યાનો ઉકેલ મળતા રાહત મળશે. પ્રોપર્ટી સંબંધિત કોઈ કાર્યમાં થોડી મુશ્કેલીઓ આવશે, પરંતુ તમે તમારી યોગ્યતા અને પ્રતિભાથી પરિસ્થિતિનો ઉકેલ લાવવામાં સક્ષમ રહેશો. પોતાનો વિકાસ કરવા માટે સ્વભાવમાં થોડી સ્વાર્થીપણું લાવવું પણ જરૂરી છે.
નેગેટિવ: કોઈ દુઃખદ સમાચાર મળવાથી મન થોડું ઉદાસ અને વ્યથિત રહેશે. રૂપિયા-પૈસાની લેવડદેવડ સંબંધિત કોઈ પણ કાર્યવાહી ન કરશો, કારણ કે તેના કારણે સંબંધો પણ બગડી શકે છે. થોડો સમય એકાંતમાં અથવા કોઈ ધાર્મિક સ્થળે પસાર કરવાથી તમને શાંતિ મળશે.
વ્યવસાય: અંગત બાબતોને કારણે તમે વ્યવસાય પર વધુ ધ્યાન આપી શકશો નહીં. પરંતુ સ્ટાફ અને કર્મચારીઓને કારણે કાર્યપ્રણાલી ઉત્તમ રીતે ચાલતી રહેશે. આ સમયે કોઈ પણ પ્રકારનું જોખમ લેવું તમને મુશ્કેલીમાં મૂકશે. વર્તમાન કાર્યપ્રણાલી પર જ ધ્યાન કેન્દ્રિત કરવું વધુ સારું છે.
લવ: વૈવાહિક સંબંધો મધુરતાપૂર્ણ રહેશે. પ્રેમ સંબંધોમાં અહમને કારણે થોડો અલગાવ આવી શકે છે.
સ્વાસ્થ્ય: ઘરના કોઈ વડીલ સભ્યના સ્વાસ્થ્યને લઈને થોડી ચિંતા રહેશે. આ સમયે તેમની યોગ્ય સંભાળ લેવાની જરૂર છે.
"""

    # Start speaking
    print("Starting Gujarati horoscope in background...")
    audio_thread = speak(horoscope_text, lang='gu', slow=False)

    # Wait for audio to finish (CRITICAL!)
    if audio_thread:
        audio_thread.join()  # This keeps main thread alive

    print("Horoscope playback completed. Good bye!")