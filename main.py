import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("It's Jarvis sir . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 35000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
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
    wish()
    while True:
        query = takeCommand().lower()
        if 'hey jarvis ' in query:
            speak('wasup raj. how are you doing')
        if 'i am doing absolutaly fine' or 'fine' or 'i am doing fine' in query:
            speak('nice to hear that')
        if 'i am not happy' in query:
            speak('it\'s ok you will feel better just do something you like')
        elif 'this pc' in query:
            os.startfile("C:")
        elif 'open books folder' in query:
            os.startfile("C:\BOOKS")
        elif 'open drivers folder' in query:
            os.startfile("C:\Drivers")
        elif 'open git tuts folder' in query:
            os.startfile("C:\git tuts")
        elif 'open jarvis folder' in query:
            os.startfile("C:\jarvis")
        elif 'open xyz folder' in query:
            os.startfile(r"C:\xyz")
        elif 'open python tutorials folder' in query:
            os.startfile(r"C:\Users\rajma\PycharmProjects\tuts")
        elif 'exit' in query:
            exit()
        elif 'chrome' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = 'https://www.google.com/'
            webbrowser.get(chrome_path).open(url)
        elif 'google classroom' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = 'https://classroom.google.com/u/0/h'
            webbrowser.get(chrome_path).open(url)
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send an email' in query:
            try:
                speak("please tell the email id of the person ")
                reciver = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                to = f"{reciver}"
                sendEmail(to, reciver)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Raj. I am not able to send this email")