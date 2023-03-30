import speech_recognition as sr
import pyttsx3 as pt3
import search as sc

# Initializing text to speech
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def main():
    speak('Hi there! this is a test, Please ask me anything.')  # First contact :)

    # speech_recognition setup
    listener = sr.Recognizer()
    listener.pause_threshold = 0.7

    with sr.Microphone() as source:  # Getting the audio from microphone
        # Listening from microphone
        print("Listening...")
        voice = listener.listen(source)

        # Recognizing the voice
        try:
            print("Processing...")
            text_result = listener.recognize_google(voice)
        except:
            print("Failed... Something is wrong")
            return

        # Try searching and speaking
        google(text_result)

        # TODO: Implement other features

        # TODO: Implement command separation and help
        # And make if there is no leading keyword it will just repeat

    # return text_result  # Returning the recognized voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def google(text):
    print("Answering...")
    search_result = sc.search(text)
    speak(search_result)


if __name__ == '__main__':
    main()
