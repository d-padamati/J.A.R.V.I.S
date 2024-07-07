import google.generativeai as genai
from time import time as t
from rich import print
import pyttsx3
import speech_recognition as sr


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





generation_config = {
 "temperature": 0.9,
 "top_p": 1,
 "top_k": 1,
 "max_output_tokens": 2048,
}

safety_settings = [
 {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
 },
 {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
 },
 {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
 },
 {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
 },
]

model = genai.GenerativeModel(
 model_name="gemini-pro",
 generation_config=generation_config,
 safety_settings=safety_settings)

genai.configure(api_key="AIzaSyCy2Wp-ssqKO9PLwMyffE13gJSWooh4U48")

messages = [
      {
          "parts": [
            {
              "text": "You are a Powerful AI Assistant Named Jarvis. Hello, How are you?"
            }
          ],
          "role": "user"
      },
      {
          "parts": [
            {
              "text": "Hello, I am doing well. How can i help you?"
            }
          ],
          "role": "model"
      }
      ]


def Gemini(prompt):
    global messages
    messages.append({
    "parts": [
      {
        "text": prompt + "***reply in less tokens***"
      }
    ],
    "role": "user"
    })
    
    response = model.generate_content(messages)

    messages.append({
    "parts": [
      {
        "text": response.text
      }
    ],
    "role": "model"})

    return response.text
def main():
    while 1:
        prompt=speechrecognition().lower()
        if (prompt.strip() == "exit"):
            break
        
        result=Gemini(prompt)
        
 
        speak(result)
