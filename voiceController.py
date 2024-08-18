import pyttsx3
import speech_recognition as sr
import serial

engine = pyttsx3.init()

port ='COM5'
baud = '9600'

ser = serial.Serial(port, baud)

def speak(audio):
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

            print("Recognizing....")

            command = r.recognize_google(audio, language ='en_in')
            print(command)

    except Exception as ex:
        print(ex)
        return "none"
    return command


def greeting():
    speak("Hello Chief! I'm you personal assistant! Please tell me How may I help you?")

if __name__ == "__main__":
    greeting()
    while True:
        command = takeCommand().lower()

        if 'on the light' in command:
            speak("turning on the lamp!")
            ser.write(b'1')

        elif 'off the lamp' in command:
            speak("turning off the lamp!")
            ser.write(b'0')
