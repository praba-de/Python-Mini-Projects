import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sounddevice as sd
import soundfile as sf

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Lily . How can I help you?")

def record_audio(duration=5, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write("command.wav", recording, fs)

def takecommand():

    r = sr.Recognizer()

    record_audio()

    with sr.AudioFile("command.wav") as source:
        audio = r.record(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query.lower()

    except:
        print("Say that again please...")
        return ""

if __name__ == "__main__":

    wishMe()

    while True:

        query = takecommand()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            webbrowser.open("https://youtube.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'exit' in query:
            speak("Goodbye")
            break