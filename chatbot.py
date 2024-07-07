import pyttsx3
import speech_recognition as sr


import google.generativeai as genai

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

def chat():


   api_key ="AIzaSyA4hRWBY-EFC8U_HuJCSHG88CgIe1bNhnE"

   genai.configure(
      api_key=api_key
   )

   model = genai.GenerativeModel('gemini-pro')
   chat = model.start_chat(history=[])


   while 1:
        qs =input("You:")
        
        if(qs.strip() == "nothing" ):
            break
            

        res = chat.send_message(qs)

        speak(f"{res.text}")

     
     
