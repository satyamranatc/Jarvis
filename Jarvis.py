import webbrowser
import os
from gtts import gTTS
import speech_recognition as sr

r = sr.Recognizer() 

Inpt = ""
Answer = ""

while True:
    try:
        with sr.Microphone() as source:       
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            Inpt = MyText
    except:
        print("Sorry, I didn't get that. Please try again.")

    if "hello" in Inpt:
        print("Hello By Jarvis")
        Answer = "Hello By Jarvis"
        tts = gTTS(text=Answer, lang='en')
        tts.save("Answer.mp3")
        os.system("afplay Answer.mp3")


    elif "goodbye" in Inpt:
        print("Bye By Jarvis")

    elif "what is your name" in Inpt:
        print("My name is Jarvis")

    elif "how are you" in Inpt:
        print("I am fine, thanks for asking")

    elif "open youtube" in Inpt:
        webbrowser.open("https://www.youtube.com/")

    else:
        print("Sorry, I didn't get that. Please try again.")