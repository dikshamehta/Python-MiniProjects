from gtts import *
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text = audio, lang = 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listen for command 

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("you said" +command+ "/n")

    #looping in case of error and continuing the program
    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#if statements for executing the commands 

def assistant(command):
    if 'open YouTube' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = "https://www.youtube.com/"
        webbrowser.get(chrome_path).open(url)

    if 'hello' in command:
        talkToMe('welcome back Chakshu')


talkToMe('what can I do for you sir')

while True:
    assistant(myCommand())









