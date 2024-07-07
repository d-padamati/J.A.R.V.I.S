import pyttsx3
import speech_recognition as sr
import pyautogui
import cv2
import pyjokes
import wikipedia
import webbrowser as wb
import subprocess
import os
from time import sleep
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pywhatkit as pwt

from clap import MainClapExe
from chatbot import chat
from aichat import main


chrome_path = '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
inbox_path ='"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
song_path ='"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
hitmusic_path ='"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
bgm_path = '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
youtube_path = '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'

#MainClapExe()


def speak(text):  
    engine =pyttsx3.init()
    Id=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice' , Id)
    print(f"J.A.R.V.I.S :{text}")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio =r.listen(source,0,8)

    try:
        print("Recognizing.....")    
        query = r.recognize_google(audio,language="en")
        print(f"You:  {query}")
        return query.lower()
    
    except:
        return ""

def openfiles():
    os.startfile(r'D:\Teja')

def date():
    date = datetime.datetime.now().strftime("%d  %m  %y")
    speak(f"The current date : {date}")
 

def greetMe():
    speak("wlcome back master")
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,master")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,master")

    else:
        speak("Good Evening,master")

def open_youtube():
        url = 'https://www.youtube.com/?bp=wgUCEAE%3D'
        wb.get(youtube_path).open(url)
    


def open_chrome():
    # url u want to open
    url = 'https://music.youtube.com/watch?v=Zfz8HUw4Ab8&list=OLAK5uy_lF3wMcyUgknWfsE1qZBR8TOCGgW655vBA'
    # Windows
    wb.get(chrome_path).open(url)

def songs():
        # url u want to open
    url = 'https://music.youtube.com/watch?v=DQ1mCl7JauI&list=RDAMVMDQ1mCl7JauI'
    # Windows
    wb.get(song_path).open(url) 

def hitmusic():
    url = 'https://music.youtube.com/watch?v=wRS8VF4y4fw&list=RDAMVMwRS8VF4y4fw'
    wb.get(hitmusic_path).open(url)

def bgm():
    url = 'https://music.youtube.com/watch?v=7QeM_rM-z6o'
    wb.get(bgm_path).open(url)


def open_mail_inbox():
    # url u want to open
    url = 'https://mail.google.com/mail/u/1/#inbox'
    # Windows
    wb.get(inbox_path).open(url)    






def Mainexecution(query):
    query =str(query).lower()

    if "hello" in query:
        speak("hello master....")

    elif "good morning" in query:
        speak("good morning master")

    elif "good afternoon" in query:
        speak("good afternoon master")

    elif "good evening " in query:
        speak("good evening master")

    elif "good night" in query:
        speak("good night master")                 
   
    elif "wake up daddy's home" in query:
        greetMe()
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        speak(f"The Time Is Now : {time}")
        date()


    elif "are you there jarvis" in query:
        speak("At your service master...")  

    elif "jarvis" in query:
        speak("yes master...")    

    elif "thank you" in query:
        speak("pleasures mine sir")      


    elif "bye" in query:
        speak("have a nice day master")    

    elif "time" in query:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        speak(f"The Time Is Now : {time}")

    elif "date" in query:
        date()


    elif "play my song" in query:
        speak("playing your favorite song master..")
        open_chrome()
    
    elif "play music" in query:
        speak("playing music")
        songs()


    elif "open mail inbox" in query:
        speak("ok master opening mail inbox")
        open_mail_inbox()



    elif "open my folder" in query:
        speak("opening your folder")
        openfiles()

           
    elif "open files" in query:
        speak('opening')   
        pyautogui.hotkey('winleft', '1') 

    elif "close files" in query:
        speak("closing...")
        pyautogui.hotkey('winleft' , '1')    


    elif "minimise window" in query:
        speak('minimising')   
        pyautogui.hotkey('winleft', 'm') 
           

    elif "maximize window" in query:
        speak('maximizing')   
        pyautogui.hotkey('winleft', 'shift','m')   


    elif "open store" in query:
         speak('opening')   
         pyautogui.hotkey('winleft', '2') 

    elif "close store" in query:
        speak("closing..")
        pyautogui.hotkey('winleft' , '2')



    elif "snip" in query:
         pyautogui.hotkey('winleft', 'shift', 's')

    elif "close this app" in query:
            # alt + f4: close this app
        pyautogui.hotkey('alt', 'f4')

    elif "open setting" in query:
        speak("opening settings")
        pyautogui.hotkey('winleft', 'i')

    elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
        pyautogui.hotkey('winleft', 'ctrl', 'd')
    elif "sleep" in query:
        speak('turning on sleep mode')   
        pyautogui.hotkey('winleft', 'l') 
        

    elif "minimise all" in query:
        speak('done master')   
        pyautogui.hotkey('winleft', 'd')

    elif "maximize all" in query:
        speak('done master')   
        pyautogui.hotkey('winleft', 'd')    
        
    elif "open this pc" in query:
        speak('opening')   
        pyautogui.hotkey('winleft', '3')  

    elif "close this pc " in query:
        speak("Closing..")
        pyautogui.hotkey('winleft' , '3')    

    elif "open whatsapp" in query:
        speak('opening')   
        pyautogui.hotkey('winleft', '5')    

    elif "close whatsapp" in query:
        speak("closing..")
        pyautogui.hotkey('winleft' , '5')    


    elif "open notepad" in query:  # if open notepad in statement
        speak("opening notepad")  # speak
        location = "C:/WINDOWS/system32/notepad.exe"  # location
        notepad = subprocess.Popen(location)  # location of a software you want tot opem

    elif "close notepad" in query:
        speak("closing notepad")
        notepad.terminate()  # terminate
            
    elif "open brave" in query:  # if open notepad in statement
        speak("opening brave")  # speak
        location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # location
        brave = subprocess.Popen(location)

    elif "close brave" in query:
        speak("closing brave")
        brave.terminate()
        
    elif "open word" in query:  # if open notepad in statement
        speak("opening word")  # speak
        location = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"  # location
        word = subprocess.Popen(location)

    elif "close word" in query:
        speak("closing word")
        word.terminate()  # terminate

    elif "open powerpoint" in query:  # if open notepad in statement
        speak("opening powerpoint")  # speak
        location = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE" # location
        powerpoint = subprocess.Popen(location) 
        
    elif "close powerpoint" in query:
        speak("closing powerpoint")
        powerpoint.terminate()  # terminate 
       
    elif "open android studio" in query:
        speak("opening android studio")
        location="C:\Program Files\Android\Android Studio\bin\studio64.exe"
        androidstudio=subprocess.Popen(location)

    elif "close android studio" in query:
        speak("closing android studio")
        androidstudio.terminate()    

        # Random jokes
    elif "joke" in query:
        speak(pyjokes.get_jokes())

        # Logout / Shutdown / Restart
    elif "logout" in query:
        speak('logging out in 5 second')
        sleep(5)
        os.system("shutdown - l")
    

    elif "shutdown" in query:
        speak('shutting down in 5 second')
        sleep(5)
        os.system("shutdown /s /t 1")

    elif "restart" in query:
        speak('initiating restart in 5 second')
        sleep(5)
        os.system("shutdown /r /t 1")  

    elif "hidden menu" in query:
        # Win+X: Open the hidden menu
        pyautogui.hotkey('winleft', 'x')

        

    elif "task manager" in query:
        # Ctrl+Shift+Esc: Open the Task Manager
        pyautogui.hotkey('ctrl', 'shift', 'esc')

    elif "task view" in query:
        # Win+Tab: Open the Task view
        pyautogui.hotkey('winleft', 'tab')

    elif "take screenshot" in query:
         # win+perscr
        pyautogui.hotkey('winleft', 'prtscr')
        speak("done")    
    
    elif "temperature" in query:
        search = "temperature in my area"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text , "html.parser")
        temp =data.find("div", class_="BNeawe").text
        speak(f"current temperature at your area is {temp}")
        # Chrome search
    elif "search" in query:
        speak("what should i search? master")
        search = speechrecognition().lower()
        speak(f"searching for {search}")
        pwt.search(search)
        speak("here what I found master")
        
    elif "open youtube" in query:
        speak("opening youtube")
        open_youtube()




    elif 'wikipedia' in query:
        speak("searching in wikipedia..")
        try:
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        except:
            print("no results found....")
            speak("no results found....")    
    
    elif "hit some music" in query:
        speak("okay master")
        hitmusic()
    elif " hit some bgms" in query:
        speak("okay master")
        bgm()
    elif "switch to chat box" in query:
        speak("switching to AI chat box")
        chat()
    

    elif "switch to bot" in query:
        speak("AI bot is online master")
        main()
            
    



        
while True:
    print("")
    query = speechrecognition()
    Mainexecution(query) 

