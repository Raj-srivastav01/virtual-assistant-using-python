from dataclasses import replace
from stringprep import map_table_b3
from importlib_metadata import metadata
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import pyautogui
import keyboard
from playsound import playsound
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 170)


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

    speak("I am wanda Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        r.dynamic_energy_adjustment_damping=0.15
        r.dynamic_energy_ratio=1.5

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    
    def whatsapp():
        speak("Tell me the Name of the person!")
        name = takeCommand()
        if 'Tanu didi' in name:
            speak("tell me the message")
            msg=takeCommand()
            speak('Tell me the time sir!')
            speak('Time in hour')
            hour=int(takeCommand())
            speak('time in minute')
            min=int(takeCommand())
            pywhatkit.sendwhatmsg("+918052895952",msg,hour,min,20)




            speak('Ok sir , Sending Whatsapp Message')
    
    def openapps():
        speak('ok sir,wait a second!')
       

        if 'screen recording' in query:
            os.startfile("C:\Program Files\Bandicam\bdcam.exe")

        elif 'Vlc media player' in query:
            os.startfile("C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")
        
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

    def closeapps():
        speak('ok sir ,wait a minute')
        if 'vs code ' in query:
            os.system('TASKKILL /F /im code.exe')

        elif 'screen recording' in query:
            os.system('TASKKILL /F /im bdcam.exe')

        elif 'Vlc media player' in query:
            os.system('TASKKILL /F /im vlc.exe')

        elif 'instagram' in query:
              os.system('TASKKILL /F /im chrome.exe')


    def Youtube():
        speak('what should i do')
        com=takeCommand()
        if 'pause' in com:
            keyboard.press('space bar')

        elif 'restart' in com :
            keyboard.press('0')

        elif 'mute' in com:
            keyboard.press('M')

        elif 'skip'in com:
            keyboard.press('l')

        elif 'reverse'in com:
            keyboard.press('j')

        elif 'full screen'in com:
            keyboard.press('F')

    def screenshot():
        speak('what should be the name of the file')
        path =takeCommand()
        pathname =path + '.png'
        path1="D:\\" + pathname
        kk=pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\")
        speak("Here is your screenshot")

    def dictionary():
        speak('Activated Dictionary mode')
        
        speak('Tell me the problem')
        pro = takeCommand()
        if 'meaning' in pro:
            pro=pro.replace("what is the",'')
            pro=pro.replace('meaning of','')
            result=PyDictionary.meaning(pro)
            speak(f'The meaning of the {pro} is {result}')

        elif 'synonym' in pro:
            pro=pro.replace("what is the",'')
            pro =pro.replace('synonym of','')
            result=PyDictionary.synonym(pro)
            speak(f'The synonym of the {pro} is {result}')

        elif 'antonym' in pro:
            pro=pro.replace("what is the",'')
            pro =pro.replace('antonym of','')
            result=PyDictionary.antonym(pro)
            speak(f'The antonym of the {pro} is {result}')
        speak("Dictionary mode exited")
    def Temp():
        search = "temperature in uttarpradesh"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem sir")



    
    





        












    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('Here is what i got for your search')
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'date' in query:
            speak('i am having headache')
        
        elif 'you single' in query :
            speak('I am in relationship with my wifi')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "srivastavraj68@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend raj bhai. I am not able to send this email")    
        
        elif 'what can you do' in query:
            speak('sir i can do many things such as')
            speak('i can tell you about anything from wikipedia')
            speak('just say wikipedia and the subject')
            speak('i can')
            speak(' open youtube')
            speak('open google')
            speak(' tell you joke ')
            speak('play any song on youtube')
            speak(' tell you time')
            speak('send mail')

        elif 'website' in query:
            speak('ok sir,launching....')
            query=query.replace("open",'')
            query=query.replace('wanda','')
            web1=query.replace('website','')
            web2='https://www.'+web1+'.com'
            webbrowser.open(web2)
            speak('Launched')

        elif 'launch' in query:
            speak('Tell me the Name of the website')
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done sir")
        
        elif 'facebook' in query :
            speak('ok sir!')
            webbrowser.open("https://www.facebook.com/")
            speak('Done sir...')

        elif 'whatsapp message' in query:
            whatsapp()

        elif 'screenshot' in query:
            screenshot()
        
        elif 'vs code' in query:
            openapps()

        elif 'screenrecorder' in query:
            openapps()

        elif 'vlc' in query:
            openapps()
        
        elif 'instagram' in query:
            openapps()

        elif 'vs code' in query:
            closeapps()

        elif 'screenrecorder' in query:
            closeapps()

        elif 'vlc' in query:
            closeapps()
        
        elif 'instagram' in query:
            closeapps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query :
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('M')

        elif 'skip'in query:
            keyboard.press('l')

        elif 'reverse'in query:
            keyboard.press('j')

        elif 'full screen'in query:
            keyboard.press('F')

        elif 'youtube tool' in query:
            Youtube()

        elif 'repeat my words' in query:
            speak('Speak sir!')
            jj=takeCommand()
            speak('You said : {jj}')

        elif 'my location 'in query:
            speak('ok sir,wait a second')
            webbrowser.open('https://www.google.com/maps/@26.8786243,81.0644255,15z')
        
        elif 'talk to me like that' in query:
            speak('I am really sorry mam')

        elif 'quit' in query:
            speak ('bye sir')
            exit()
        elif 'shut down'in query:
            os.system("shutdown /s /t 1")

        elif 'where is' in query:
            speak('i am trying to find the location you asked for')
            speak('found sir')
            query=query.replace("where is",'')
            loc1=query.replace('wanda','')
            loc2='https://www.google.com/maps/place/'+loc1
            webbrowser(loc2)
        
        elif 'you bitch' in query:
            speak('mam then i would also be of your biradari')
        
        elif 'shut up' in query:
            speak('you go to hell')

        elif 'alarm' in query:
            speak("Enter the time")
            time = input("Enter the time :")
            while True:
                time_A=datetime.datetime.now()
                now = time_A.strftime("%H:%M:%S")
                if now == time:
                    speak ("Time to wakeup sir")
                    playsound("C:\Raj\TOKYODRIFT.mp3")
                    speak("Alarm closed")

                elif now>time :
                    break

        elif 'dictionary mode' in query :
            dictionary()

        elif 'temperature' in query:
            Temp()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())
        
        elif "enter" in query:
            keyboard.press("Enter")

        elif'exit' in query:
            speak('Bye sir')
            exit()
        
