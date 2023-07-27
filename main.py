import os
import openai
from os.path import join,dirname
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np


openai.api_key = "YOUR API KEY"
openai.api_base = 'https://api.pawan.krd/v1'
model = 'gpt-3.5-turbo'

# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice' , 'english-us')


# Listen for the wake word "hey pos"
def listen_for_wake_word(source):
    # print("Listening...")
    engine.say("Listening")
    engine.runAndWait()

    while True:
        audio = r.listen(source)
        try:
            # print('SAY')
            text = r.recognize_google(audio)
            print(text)
            if "wake up GPT" or "I have another question" in text.lower():
                print("Wake word detected.")
                engine.say("Yes master")
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass

# Listen for input and respond with OpenAI API
def listen_and_respond(source):
    # print("Listening...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue

            # Send input to OpenAI API
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}]) 
            response_text = response.choices[0].message.content
            print(f"OpenAI response: {response_text}")

            # Speak the response
            engine.say(response_text)
            engine.runAndWait()
            time.sleep(3)

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(5)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break

# Use the default microphone as the audio source
with sr.Microphone() as source:
    listen_for_wake_word(source)
