from sys import exit
import speech_recognition as sr
import pyttsx3 as pt3
from search import search
from pywhatkit import playonyt
from wikipedia import summary, exceptions

# Initializing text to speech
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def main():
    # Getting command and split into key and content
    keyword, content = ('', '')  # Bad practice :(
    command = get_command()
    try:
        keyword, content = command.split(' ', 1)
    except ValueError:
        command_list()
    print(f'command: {keyword}, content: {content}')

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
    speak('Hi there! this is a test')  # First contact :)

    # speech_recognition setup
    listener = sr.Recognizer()
    listener.pause_threshold = 0.7

    with sr.Microphone() as source:  # Getting the audio from microphone
        # Listening from microphone (converting audio data)
        print('Listening...')
        voice = listener.listen(source, phrase_time_limit=5)

        # Recognizing the voice
        try:
            print('Processing...')
            text_result = listener.recognize_google(voice)
        except:
            print('Failed... Something went wrong, exiting...')
            exit(1)

    return text_result


def speak(text):
    engine.say(text)
    engine.runAndWait()


def command_list():
    print('command list: Search, Wiki, Open (video, not good), ')
    speak('please specify the command')
    exit(2)


def google(text):
    print('Searching...')
    search_result = search(text)
    print('Answering...')
    print(f'Google: {search_result}')
    speak(search_result)


def youtube(text):
    speak(f'opening {text}')
    print(f'"{text}" opening...')
    playonyt(text)


def wikipedia(text):
    print('Searching...')
    try:
        wiki_result = summary(text, sentences=5, auto_suggest=True)
    except exceptions.DisambiguationError as exception:  # If not found
        print('Not found...')
        speak(f'I could not find {text}')

        # List suggestion
        print(exception)
        speak(exception)
        exit(3)

    print(f'Wikipedia: {wiki_result}')
    speak(wiki_result)


if __name__ == '__main__':
    main()
