import speech_recognition as sr
import pyttsx3 as pt3

# Initializing text to speech
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def command():
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
            service = listener.recognize_google(voice)
            print(service)
        except:
            pass
        # return service  # Returning the recognized voice


# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    command()
