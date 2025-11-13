from gtts import gTTS
import os

# Hindi
# text_hindi = "नमस्ते! आप कैसे हैं? यह हिंदी में टेक्स्ट-टू-स्पीच है।"
# tts_hindi = gTTS(text=text_hindi, lang='hi')
# tts_hindi.save("hindi_output.mp3")

# Gujarati
text_guj = "હેલો! તમે કેમ છો? આ ગુજરાતીમાં છે."
tts_guj = gTTS(text=text_guj, lang='gu')
tts_guj.save("gujarati_output.mp3")

# Play (optional)
os.system("start gujarati_output.mp3")      # Windows
# os.system("open hindi_output.mp3")     # macOS
# os.system("xdg-open hindi_output.mp3") # Linux