from sys import exit

import pyttsx3 as pt3
import speech_recognition as sr
from pywhatkit import playonyt
from wikipedia import summary, exceptions

from search import search, speed

# Initializing text to speech
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def main():
    # Getting command and split into key and content
    keyword, content = ('', '')  # Bad practice :(
    command = get_command()

    # Exit condition check
    if command == 'goodbye':
        print('Exiting...')
        speak('good bye, see you again')
        exit(0)
    if command == 'exit' or command == 'stop':
        print('Exiting...')
        exit(1)

    # Check without content
    if 'check' in command:
        if 'internet' in command or 'speed' in command:
            speed_test()
            return

    try:
        keyword, content = command.split(' ', 1)
    except ValueError:
        command_list()
        return
    print(f'command: {keyword}, content: {content}')

    # Do operation based on keyword
    match keyword.lower():
        case 'search':
            google(content)
        case 'open':
            youtube(content)
        case 'wiki':
            wikipedia(content)
        case _:
            command_list()


def get_command():
    speak('you can ask me something')

    # speech_recognition setup
    listener = sr.Recognizer()
    listener.pause_threshold = 0.7

    with sr.Microphone() as source:  # Getting the audio from microphone
        # Listening from microphone (converting audio data)
        print('Listening...')
        voice = listener.listen(source, phrase_time_limit=5)

        # Recognizing the voice
        print('Processing...')
        try:
            text_result = listener.recognize_google(voice)
        except sr.exceptions.UnknownValueError:
            print('Failed... Something went wrong')

    try:
        return text_result
    except UnboundLocalError:
        return ''


def speak(text):
    engine.say(text)
    engine.runAndWait()


def command_list():
    print('command list: Search, Wiki, Open (video, not good except music...), , goodbye (exit program), '
          'exit / stop')
    speak('I do not understand, please repeat.')


def google(text):
    print(f'Searching {text}...')
    search_result = search(text)
    print('Answering...')
    print(f'Google: {search_result}')
    speak(search_result)


def youtube(text):
    speak(f'opening {text} on YouTube')
    print(f'"{text}" opening...')
    playonyt(text)
    exit(2)


def wikipedia(text):
    wiki_result = text  # Bad practice
    print(f'Searching {text}...')
    try:
        wiki_result = summary(text, sentences=4)
    except exceptions.DisambiguationError as exception:  # If not found
        print('Not found...')
        speak(f'I could not find {text}')

        # List suggestion
        print(exception)
        speak(exception)
    except exceptions.PageError:
        print('Not found...')
        speak('I am unable to find the page.')

    print(f'Wikipedia: {wiki_result}')
    speak(wiki_result)


def speed_test():
    print('Checking...')
    print('This may take a while')
    speak('checking your internet speed, please wait patiently')
    down, up = speed()
    print(f'download: {down:.2f}MB, upload {up:.2f}MB')
    speak(f'your download speed is {down:.2f}Mega Bytes and'
          f'your upload speed is {up:.2f}Mega Bytes')


if __name__ == '__main__':
    speak('Hi there! I am an AI?')  # First contact :)
    while True:
        main()
