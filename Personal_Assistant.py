import pyttsx3
from pywhatkit.core.core import HEIGHT 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyaudio
from googlesearch import search
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pywhatkit
import pyautogui as pg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_path = 'C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe %s'

#Setting voice of our Assistant 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Speak function will speak the audio passed to it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        #print(sr.Microphone.list_microphone_names()) #print all the microphones connected to your machine
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()\
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")

    elif 'open google' in query:
        webbrowser.open("https://www.google.co.in/")

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"The time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)      

    elif 'search' and 'google' in query:
        sentence = query.split(" ")
        word = sentence[1]
        webbrowser.open(f"https://www.google.co.in/search?q={word}")

    elif 'play music' in query:
        sentence = query.split(" ")
        song_list = sentence[2:]
        for items in song_list:
            if items<1:
                speak(" Did not recognise song, Please try again")
            if 1<=items<2:
                song = song_list
            if items>2:
                song = "%20".join(song_list)
        try:
            driver = webdriver.Chrome("G:\\webdr\\chromedriver.exe")
            driver.get(f"https://gaana.com/search/{song}")
            driver.maximize_window()
            time.sleep(3)
            driver.find_element_by_class_name("card").click()
            time.sleep(3)
            driver.find_element_by_id("playBtn1").click()

        except Exception as e:
            print(e)
            print("Song not found, please try again")
            speak("Song not found, please try again")

    elif 'whatsapp' in query:
        sentence = query.split(" ")
        reverse_query = sentence[::-1]
        person_name = reverse_query[0].lower() 
        speak("What message do you want to send")
        print("What message do you want to send")
        user_message = takeCommand()
        if person_name=="abc:
            pywhatkit.sendwhatmsg_instantly("+91**********",user_message)
            time.sleep(50)
            pg.press("enter")
            print("Successfully Sent!")
            speak("Successfully Sent!")
        
