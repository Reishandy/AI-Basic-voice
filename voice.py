import speech_recognition as sr
from asyncio import get_event_loop
from playsound import playsound
from os import path

import edge_tts

listener = sr.Recognizer()
listener.pause_threshold = 0.7

voices = [
    'id-ID-GadisNeural',
    'en-US-AnaNeural', 'en-US-JennyNeural', 'en-US-AriaNeural',
    'en-GB-MaisieNeural', 'en-GB-SoniaNeural', 'en-GB-LibbyNeural',
    ]
language = ['id-ID', 'en-US', 'en-GB']


def get_command():
    while True:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source, phrase_time_limit=6)

            print('Processing...')
            try:
                text_result = listener.recognize_google(voice, language=language[1])
                print(f'> {text_result}')
            except sr.exceptions.UnknownValueError:
                print('Not recognized, Please repeat...')

        try:
            return text_result
        except UnboundLocalError:
            continue


def speak(text):
    async def _main() -> None:
        communicate = edge_tts.Communicate(text, voices[2])
        await communicate.save('voice.mp3')

    get_event_loop().run_until_complete(_main())
    playsound(path.dirname(__file__) + '\\voice.mp3')


if __name__ == '__main__':
    while True:
        speak(get_command())
