import win32com.client
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import datetime
import os
from openai import OpenAI
import re
import time

speaker = win32com.client.Dispatch('SAPI.SpVoice')
print("Hello this is jarvis Ai")
speaker.speak("Hello this is jarvis AI")



def say(text):
    speaker.speak(text)
    return text
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 1
        try :
            audio = r.listen(source)
            query = r.recognize_google(audio,language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e :
            return "Some error occered sorry by jarvis"        

def Ai_response(prompt):     
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key="Api_key here"
    )

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.1:fireworks-ai",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    response = completion.choices[0].message.content
    clean_response = re.sub(r"[*#`_>]", "", response)
    print(clean_response)
    return clean_response

chatstr = ""
def chat(prompt):
    
    client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="Api_key here"
    )

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.1:fireworks-ai",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    response = completion.choices[0].message.content
    clean_res = response.split("</think>")[-1].strip()
    clean_res = re.sub(r'[*#`_>]',"",clean_res)
    print(f"jarvis : {clean_res}\n")
    # clean_response = re.sub(r"[*#`_>]", "", response)
    # print(clean_response)
    return response

while True :
    print("Listning......")
    query = takeCommand()
    #say(query)
    sites = [["Youtube","https://youtube.com"],["wikipediea","https://wikipedia.com"],["Instagram","https://instagram.com"],
             ["Google","https://www.google.com"],["GitHub","https://github.com/zakwan-haaziq-2006?tab=repositories"],['LinkedIn',"https://www.linkedin.com/feed/"]]
    for site in sites :
        if f"{site[0]}".lower() in query.lower() :
            webbrowser.open(site[1])
            say(f"Opening {site[0]} sir")
        # elif "instagram" in query.lower():
        #     webbrowser.open("https://instagram.com")
        #     say("Opening Instagram sir")
    
    if "play music" in query.lower():
        musicpath = "C:/Users/Zakwan/Music/Musics/Mula mere.mp3"
        say("Playing music sir")
        os.startfile(f"{musicpath} ")
        
    
    elif "the time" in query.lower():
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        AmPm = datetime.datetime.now().strftime("%p")
        say(f"Sir the time is {hour} : {min} {AmPm}")
        
    elif "open msword".lower() in query.lower():
        os.system(f"start "" C:/Program Files/Microsoft Office/root/ce16/WINWORD.exe")
        
    elif "using ai" in query.lower() :
        try :
            inp_prompt = query.lower().split("ai ")
            #print(inp_prompt[1])
            response = Ai_response(inp_prompt[1])
            cleaned = response.split("</think>")[-1].strip()
            print("just A second.. Ai is responding")
            print(cleaned)
            say(cleaned)
        except Exception as e :
            say("Sorry. Some error occured Please ask again...")
    
    elif "stop" in query.lower():
        exit()
            

    else :
        if "open" in query.lower():
            continue
        res = chat(query.lower())
        clean = res.split("</think>")[-1].strip()
        say(clean)
        

        