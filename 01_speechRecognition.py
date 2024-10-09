import speech_recognition as sr

def ask(q: str):
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print(q)
                audio = recognizer.listen(source)
                ans = recognizer.recognize_google(audio)
                return ans
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")
            except sr.RequestError:
                print("Sorry, there seems to be an issue with the speech recognition service.")
            
if __name__=="__main__":
    name = ask("What is your name?")
    print(f"Thank you {name}, for your time.")
