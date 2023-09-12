import pyttsx3 #installed #it is text to speech conversion library
import datetime #inbuilt
import speech_recognition as sr #installed
import wikipedia #installed
import webbrowser #inbuilt #to access browsers
import os # inbuilt # to access computer files
import random


engine = pyttsx3.init('sapi5') #microsoft inbuilt speech api to take voices
voices = engine.getProperty('voices')
#print(voices[1].id) #you can add more voices there are majorly two inbuilt voices male and female
engine.setProperty('voice',voices[0].id)

def speak(audio): #function for speaking loud in microsoft ai assistant
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning!")

    elif hour>12 and hour<16:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("hello sir! i am bloomer. how may i help you?")


def takeCommand(): #takes microphone input from user and return string  output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognising......")
        query= r.recognize_google(audio , language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing task based on query

        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences = 2)
            speak("According to the wikipedia")
            print(results)
            speak(results)

        elif  'open youtube' in query:
            webbrowser.open("youtube.com")

        elif  'open google' in query:
            webbrowser.open("google.com")

        elif  'open spotify' in query:
            webbrowser.open("spotify.com")

        elif  'play music' in query:
            music_dir= 'E:\\Python projects\\songs'
            songs = os.listdir(music_dir)
            #song = random.choices(songs) 
            print(songs)

            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'time'in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        
        elif 'who are you' in query:
            speak("I am your AI assistant bloomer sir")
           

        elif 'open code' in query:
            code_path = "E:\\IntelliJ IDEA Community Edition 2022.3.2\\bin\\idea64.exe"
            os.startfile(code_path)
            
        
        

           





