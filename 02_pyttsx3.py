import pyttsx3 as tts


engine=tts.init()
engine.setProperty('rate',125) # default 200
engine.setProperty('volume',1) 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0 for male


engine.say("Shut up Fatima")


engine.runAndWait()


