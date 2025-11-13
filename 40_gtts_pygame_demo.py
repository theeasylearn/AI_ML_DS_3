import os
import tempfile
import threading
import pygame
from gtts import gTTS

# Initialize pygame mixer (must be done once)
pygame.mixer.init()

def speak(text, lang='hi', slow=False):
    """
    Convert text to speech and play in background using pygame.
    No window opens. Supports Hindi, Gujarati, etc.
    """
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tmp_file = fp.name

    # Generate speech
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(tmp_file)

    # Play in background thread
    def play_and_cleanup():
        try:
            pygame.mixer.music.load(tmp_file)
            pygame.mixer.music.play()
            # Wait until playback finishes
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        finally:
            # Clean up temp file
            try:
                os.unlink(tmp_file)
            except:
                pass

    thread = threading.Thread(target=play_and_cleanup, daemon=True)
    thread.start()

# ——— EXAMPLE USAGE ———
if __name__ == "__main__":
    # # Hindi
    # speak("नमस्ते! यह पाइगेम के साथ बैकग्राउंड में चल रहा है।", lang='hi')

    # Gujarati
    speak("""
પોઝિટિવ: છેલ્લા કેટલાક સમયથી ચાલી રહેલી સમસ્યાનો ઉકેલ મળતા રાહત મળશે. પ્રોપર્ટી સંબંધિત કોઈ કાર્યમાં થોડી મુશ્કેલીઓ આવશે, પરંતુ તમે તમારી યોગ્યતા અને પ્રતિભાથી પરિસ્થિતિનો ઉકેલ લાવવામાં સક્ષમ રહેશો. પોતાનો વિકાસ કરવા માટે સ્વભાવમાં થોડી સ્વાર્થીપણું લાવવું પણ જરૂરી છે.

નેગેટિવ: કોઈ દુઃખદ સમાચાર મળવાથી મન થોડું ઉદાસ અને વ્યથિત રહેશે. રૂપિયા-પૈસાની લેવડદેવડ સંબંધિત કોઈ પણ કાર્યવાહી ન કરશો, કારણ કે તેના કારણે સંબંધો પણ બગડી શકે છે. થોડો સમય એકાંતમાં અથવા કોઈ ધાર્મિક સ્થળે પસાર કરવાથી તમને શાંતિ મળશે.

વ્યવસાય: અંગત બાબતોને કારણે તમે વ્યવસાય પર વધુ ધ્યાન આપી શકશો નહીં. પરંતુ સ્ટાફ અને કર્મચારીઓને કારણે કાર્યપ્રણાલી ઉત્તમ રીતે ચાલતી રહેશે. આ સમયે કોઈ પણ પ્રકારનું જોખમ લેવું તમને મુશ્કેલીમાં મૂકશે. વર્તમાન કાર્યપ્રણાલી પર જ ધ્યાન કેન્દ્રિત કરવું વધુ સારું છે.

લવ: વૈવાહિક સંબંધો મધુરતાપૂર્ણ રહેશે. પ્રેમ સંબંધોમાં અહમને કારણે થોડો અલગાવ આવી શકે છે.

સ્વાસ્થ્ય: ઘરના કોઈ વડીલ સભ્યના સ્વાસ્થ્યને લઈને થોડી ચિંતા રહેશે. આ સમયે તેમની યોગ્ય સંભાળ લેવાની જરૂર છે.
""", lang='gu', slow=False)

    # # English
    # speak("Hello! Playing silently with pygame.", lang='en')

    # Keep main thread alive while audio plays
    import time
    print("Playing audio in background... (10 seconds)")
    time.sleep(10)
    print("Done!")