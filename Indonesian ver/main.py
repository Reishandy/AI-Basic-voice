from sys import exit
from os import path

import speech_recognition as sr
from pywhatkit import playonyt
from wikipedia import summary, exceptions, set_lang
from gtts import gTTS
from playsound import playsound

from search import search


def main():
    # Getting command and split into key and content
    keyword, content = ('', '')  # Bad practice :(
    command = get_command()

    # Exit condition check
    if command == 'selamat tinggal':
        print('Keluar...')
        speak('Sampai jumpa')
        exit(0)
    if command == 'keluar' or command == 'stop':
        print('Keluar...')
        exit(1)

    try:
        keyword, content = command.split(' ', 1)
    except ValueError:
        command_list()
        return
    print(f'command: {keyword}, content: {content}')

    # Do operation based on keyword
    match keyword.lower():
        case 'cari':
            google(content)
        case 'buka':
            youtube(content)
        case 'wiki':
            wikipedia(content)
        case _:
            command_list()


def get_command():
    speak('katakan sesuatu')

    # speech_recognition setup
    listener = sr.Recognizer()
    listener.pause_threshold = 0.9

    with sr.Microphone() as source:  # Getting the audio from microphone
        # Listening from microphone (converting audio data)
        print('Mendengarkan...')
        voice = listener.listen(source, phrase_time_limit=5)

        # Recognizing the voice
        try:
            print('Memproses...')
            text_result = listener.recognize_google(voice, language='id-ID')
        except sr.exceptions.UnknownValueError:
            print('Gagal... Ada sesuatu yang salah')

    try:
        return text_result
    except UnboundLocalError:
        return ''


def command_list():
    print('Perintah: Cari, Wiki, Buka (video, not good except music...), selamat tinggal (keluar program), '
          'keluar / stop')
    speak('Saya tidak mengerti, mohon diulangi.')


def google(text):
    print(f'Mencari {text}...')
    search_result = search(text)
    print('Menjawab...')
    print(f'Google: {search_result}')
    speak(search_result)


def youtube(text):
    speak(f'membuka {text} di YouTube')
    print(f'"{text}" sedang dibuka...')
    playonyt(text)
    exit(2)


def wikipedia(text):
    set_lang('id')
    wiki_result = text  # Bad practice
    print(f'Mencari {text}...')
    try:
        wiki_result = summary(text, sentences=4)
    except exceptions.DisambiguationError as exception:  # If not found
        print('Tidak ditemukan...')
        speak(f'Saya tidak bisa menemukan {text}')

        # List suggestion
        speak('apakah yang dimaksud')
        print(exception)
        speak(exception)
    except exceptions.PageError:
        print('Tidak ditemukan...')
        speak(f'Saya tidak bisa menemukan {text}')

    print(f'Wikipedia: {wiki_result}')
    speak(wiki_result)


def speak(text):
    speaking = gTTS(text, lang='id')
    speaking.save('voice.mp3')
    playsound(path.dirname(__file__) + '\\voice.mp3')


if __name__ == '__main__':
    speak('Halo, saya adalah AI')  # First contact :)
    while True:
        main()
