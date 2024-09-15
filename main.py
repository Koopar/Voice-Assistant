import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry, can't understand")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        data1 = sptext()

        if "your name" in data1:
            name = "My name is Tony"
            speechtx(name)
        elif "how old are you" in data1:
            age = "I am immortal"
            speechtx(age)
        elif "hello" in data1:
            greeting = "Hello,Good to see you"
            speechtx(greeting)


        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx("The current time is " + time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'erp' in data1:
            webbrowser.open("https://erp.skit.ac.in/signin/index")
        elif 'spotify' in data1:
            webbrowser.open("https://open.spotify.com/")
        elif 'google' in data1:
            webbrowser.open("https://www.google.com/")
        elif 'india' in data1:
            india = "Mr.narendra modi"
            speechtx(india)

        elif 'gmail' in data1:
            webbrowser.open("https://mail.google.com/mail/u/1/?ogbl#inbox")
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
        elif 'play music' in data1:
            music_folder = "D:\\movies"  # Change this to the correct folder path
            listsong = os.listdir(music_folder)
            if listsong:
                print(listsong)
                os.startfile(os.path.join(music_folder, listsong[1]))  # Play the first song
            else:
                speechtx("No songs found in the music folder.")
        elif "exit" in data1:
            speechtx("Thank You")
            break
