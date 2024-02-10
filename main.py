from characterai import PyCAI
import os

client = PyCAI(os.environ['CharacterAI'])

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
        print('\n')
        message = input('You: ')
        data = client.chat.send_message(chat['external_id'], tgt, message) 
        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']
        print('\n')
        print(f"{name}: {text}",end='\n')

try:
    char = Assistant
    chat = client.chat.get_chat(char)

    InitializeChat(chat)
except Exception as e:
    print(f"ERROR: {e}")
