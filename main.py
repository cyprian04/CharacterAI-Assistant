import os
import time
from playsound import playsound
from gtts import gTTS
from characterai import PyCAI
import speech_recognition as sr

client = PyCAI(os.environ['CharacterAI'])
said = ''
#Characters
Yukana_Yame = 't37V6MiLGyUynkHZo-m49MVz4YDyY89Mjmm2DSg8aPo'
Two_B       = 'csTC3hw0Fnj1Whnl0uV1Nb3_oYIillMQtdBH5NEl0Gs'
Nami        = 'CPzWLN939JIlyNVKosDwU1Tc2yS3eylbMTqLfHxPYYs'
Assistant   = 'YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8'
Rias        = '_kvcCUxfU5zVA00JZLtpYm0LIHSVXjchcYNwlNAh9cs'

def InitializeChat(chat):
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    while True:
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("SPEAK NOW", end='\n')
            audio = r.listen(source)

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print(f"speak ERROR: {e}")

        print('\n')
        message = str(said)
        data = client.chat.send_message(chat['external_id'], tgt, message) 
        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']
        print('\n')
        print(f"{name}: {text}",end='\n')
        speech = gTTS(text=text, lang='en',slow=False, tld='com.au')
        speech.save("welcome.mp3")
        playsound("welcome.mp3")
        time.sleep(10)
        
try:
    chat = client.chat.get_chat(Assistant)
    InitializeChat(chat)

except Exception as e:
    print(f"ERROR: {e}")
