from datetime import datetime
from sys import exit

from pywhatkit import playonyt
from wikipedia import summary, exceptions

import rps
from search import search, speed
from voice import get_command, speak


def main():
    # Getting command and split into key and content
    command = get_command().lower()

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
        case 'play':
            if content == 'rock paper scissors':
                rps.play()
            else:
                print('Rock Paper Scissors')
        case 'what':
            date = 'I do not know'
            if 'time' in content:
                date = get_date_or_time(use_time=True)
            if 'date' in content:
                date = get_date_or_time(use_date=True)
            if 'day' in content:
                date = get_date_or_time(use_day=True)
            if 'date' in content and 'day' in content:
                date = get_date_or_time()
            print(date)
            speak(f'It is {date}')
        case _:
            command_list()


def command_list():
    print('command list: Search, Wiki, Open (video, not good except music...), check internet speed, play: rps'
          ', ask for day time and date, goodbye (exit program), exit / stop')
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


def get_date_or_time(use_date=False, use_time=False, use_day=False):
    date = datetime.now()
    if use_date:
        return date.strftime('%d %B %Y')
    elif use_time:
        return date.strftime('%H %M')
    elif use_day:
        return date.strftime('%A')
    else:
        return date.strftime('%H %M %A %d %B %Y')


if __name__ == '__main__':
    speak('Hi there! I am an AI. ask me something')  # First contact :)
    while True:
        main()
