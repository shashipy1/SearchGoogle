import pyttsx3                   #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia                 #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():  # wish me a/c to time and use of speak fun
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("HARE KRISHNA ")
    elif hour>=12 and hour<=18:
        speak("Hare ram")
    else:
        speak("Radhe radhe ")
    # speak("I am google, PLEASE TELL ME HOW CAN I HELP YOU")

def takeCommand():      # IT TAKE MICROPHONE INPUT FROM USERS AND RETURN STRING OUTPUT
    r = sr.Recognizer()    # for recognize the audio
    with sr.Microphone() as s:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        # print("going to Listening..")
        audio = r.listen(s)
        print("Listening ended|")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
        speak(query)
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shashikant.py8@gmail.com', 'shashi@1999')
    server.sendmail('shashikantssm6@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # speak("shashi is good boy and also coder, pythoneer")
    wishMe()
    # takeCommand() # it takes values as a string

    # while True:
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'ok google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
    
        elif 'play music' in query:
            music_dir = 'E:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
    
        elif 'open code' in query:
            codePath = "E:\\All Softwares\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    
        elif 'email to shashi' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "shashiyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! shahi bhai, I am not able to send mail")


        elif 'google sheet' in query:
            webbrowser.open("docs.google.com/spreadsheets/d/14liQ1cRTtuVfwC4MGHZYK3QlBCoU86fplL6TiwIeRLc/edit#gid=1199454067&range=332:332")

        elif 'quit' in query:
            print(quit)
            break