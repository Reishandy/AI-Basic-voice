import speech_recognition as sr
import pyttsx3 as pt3
import search as sc

# Initializing text to speech
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def main():
    listener = sr.Recognizer()  # speech_recognition module holder
    with sr.Microphone() as source:  # Getting the audio from microphone
        speak('Hi there! this is a test')  # First contact :)

        # Listening from microphone
        print("Listening...")
        listener.pause_threshold = 0.6
        voice = listener.listen(source)

        # Recognizing the voice
        try:
            print("Processing...")
            text_result = listener.recognize_google(voice)

            # Try searching and speaking
            search(text_result)
        except:
            print("Failed... Something is wrong")

    # return text_result  # Returning the recognized voice


# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


def search(text):
    print("Answering...")
    search_result = sc.search(text)
    speak(search_result)


if __name__ == '__main__':
    main()
