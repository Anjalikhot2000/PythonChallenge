import pyttsx3
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import wolframalpha
import os
import sys

# Choose an alternative speech recognition library
# (Replace 'alternative_library' with your preferred choice)
alternative_library = None  # Example: import googletrans  # For Google Speech-to-Text

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    elif currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you?')

def myCommand():
    if alternative_library is not None:
        # Use the chosen alternative library for speech recognition
        # (Replace the following with the specific implementation of your chosen library)
        query = alternative_library.recognize_google(audio, language='en-in')  # Example
    else:
        # Fallback to user input if no alternative library is available
        speak('Speech recognition is not available. Please type your command:')
        query = input('Command: ')

    return query.lower()

if __name__ == '__main__':

    while True:
        query = myCommand()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        # ... (rest of your code remains the same) ...

        else:
            speak('Next Command! Sir!')