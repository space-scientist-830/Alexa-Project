import speech_recognition as speech

def speechrecog():
     r = speech.Recognizer() 
     with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
     command=r.recognize_google(audio)
     print("You said" + command)
     return command 
 
words=speechrecog()


