import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I hellp you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('s1062210188@timscdrmumbai.in', 'Ranjeet@08')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            # 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            # speak('Searching Wikipedia...')
            # query = query.replace("wikipedia", "")
            # results = wikipedia.summary(query, sentences=2) 
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'word document' in query:
            codePath = "C:\\Program Files\Microsoft Office\\root\\Office16\\WINWORD.EXE" 
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to Ranjeet' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "sranjeetkumar0811@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")