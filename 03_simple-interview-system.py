import speech_recognition as sr
import pyttsx3 as tts
import os

def say(sent:str):
    engine=tts.init()
    engine.setProperty("rate",125)
    engine.say(sent)
    engine.runAndWait()
    return

def listen():
    with sr.Microphone() as source:
        recognizer=sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        chk=3
        while chk:            
            print("Speak:")
            audio=recognizer.listen(source)
            try:
                text=recognizer.recognize_google(audio)
                os.system("cls")
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")
                chk-=1
            except sr.RequestError:
                print("Sorry, there seems to be an issue with the speech recognition service.")
                chk-=1
            chk-=1
        os.system("cls")  
    return '-1'

def createReport(ques:str,ans:str,filename:str):
    with open(filename,'a') as file:
        file.write("Question: "+ques+"\n")
        file.write("Answer: "+ans+"\n\n")
        
    return

def report(id:int):
    ques=[
        "What is your full name?",
        "Can you tell me where you're from?",
        "What is your educational background?",
        "Where did you study?",
        "Can you share a little bit about your family?",
        "Where are you currently residing?", 
        "Are you open to relocating if necessary?",
        "What hobbies or activities do you enjoy outside of work?",
        "What languages do you speak fluently?",
        "How would your friends or family describe you?",
        "What motivates you both personally and professionally?"
    ]
    for q in ques:
        say(q)
        ans=listen()
        if ans=="-1":
            print("Skiping the question due to issues.")
            continue
        createReport(q,ans,"interviewee"+str(id)+'.txt')

if __name__=="__main__":
    report(1001)
    
    

            