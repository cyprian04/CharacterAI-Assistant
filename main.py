import os
import time
import vlc
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

def play_sound_with_vlc(text):
    speech = gTTS(text=text, lang='en', slow=False, tld='com.au')
    speech.save("welcome.mp3")

    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    media = instance.media_new("welcome.mp3")
    player.set_media(media)

    media_list_player = instance.media_list_player_new()
    media_list = instance.media_list_new(["welcome.mp3"])
    media_list_player.set_media_list(media_list)
    media_list_player.set_media_player(player)
    media_list_player.play()

    while media_list_player.get_state() != vlc.State.Ended:
        time.sleep(1)
        
    media_list_player.release()
    player.release()

def initialize_chat(chat):
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
        message = (said)
        data = client.chat.send_message(chat['external_id'], tgt, message)
        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']
        print('\n')
        print(f"{name}: {text}", end='\n')
        play_sound_with_vlc(text)

try:
    chat = client.chat.get_chat(Assistant)
    initialize_chat(chat)

except Exception as e:
    print(f"ERROR: {e}")
