import pyaudio
import sounddevice as sd
import numpy as np
import pyttsx3



threshold = 40
Clap = False


def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm =np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        print("Claped!")
        Clap = True
   

def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)
    
def speak(text):  
    engine =pyttsx3.init()
    Id=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice' , Id)
    print(f"J.A.R.V.I.S :{text}")
    engine.say(text=text)
    engine.runAndWait()



def MainClapExe():    
    while True:
        Listen_for_claps()
        if Clap == True:
            speak("Jarvis is online master..") 
            speak("how can i help you master")
            break
        else:
            pass

