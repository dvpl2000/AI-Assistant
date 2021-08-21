import pyttsx3 as pyt
from datetime import datetime as dt
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import psutil as ps
import pyjokes
import os
import pyautogui as pg
import json
import requests
from urllib.request import urlopen

engine=pyt.init()

Time=dt.now().strftime("%H:%M")
Date=dt.now().strftime("%d,%m,%Y")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(): 
    hour = dt.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Divyansh")
        speak(f"The current time is {Time} and the current date is {Date}")

    elif hour >=12 and hour<18:
        speak("Good Afternoon Tanishq!")
        speak(f"The current time is {Time} and the current date is {Date}")
        
    elif hour >=18 and hour <24:
        speak("Good Evening Tanishq!")
        speak(f"The current time is {Time} and the current date is {Date}")

    else:
        speak("Good Night Tanishq!")
        speak(f"The current time is {Time} and the current date is {Date}")

    speak("I am at your service. Please tell me how can I help you?")
    
def takecommand_():
    speech=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speech.pause_threshold=1
        audio=speech.listen(source)

    try:
        print("Recognizing...")
        query=speech.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:
        print(e)
        print("Sorry, I did'nt get it...Say that again...")
        return "None"
    return query

def screenshot():
    ss=pg.screenshot()
    ss.save("C:/Users/Tanishq/Desktop/Data Science/AI Assistant/ss.png")

def cpu_():
    usage=str(ps.cpu_percent())
    speak("cpu is at "+usage)

    battery=ps.sensors_battery()
    battery_percent=str(battery.percent)
    speak("the battery is at")
    speak(battery_percent+" percent")

if (__name__=="__main__"):
    
    wishme()
    while True:
        query=takecommand_().lower()
        
        if "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wk.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif "search chrome" in query:
            speak("tell me the query")
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search_chrome=takecommand_().lower()
            wb.get(path).open_new_tab(search_chrome+'.com')
        
        elif "search youtube" in query:
            speak("what should i search")
            search_youtube=takecommand_().lower()
            speak("taking you to youtube")
            wb.open("https://www.youtube.com/results?search_query="+search_youtube)

        elif "search google" in query:
            speak("what should i search")
            search_google=takecommand_().lower()
            wb.open("https://www.google.com/search?q="+search_google)

        elif "cpu" in query:
            cpu_()

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "stop" in query:
            break

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand_()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = takecommand_()
            if 'yes' in dt or 'sure' in dt:
                strTime = dt.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)

        elif "screenshot" in query:
            screenshot() 

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "") 

        
        elif 'news' in query:
            
            try:

                json_file = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey={YOUR API KEY}')
                data = json.load(json_file)
                i = 1
                
                speak('top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e))
        
        elif 'offline' in query:
            speak("going Offline")
            quit()



        

       

    


