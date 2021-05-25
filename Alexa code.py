#import speech_recognition as S
import pygame 
import pyttsx3
import time
import speech_recognition as speech
EventStatus='None'
Alscreen=[]
Alimg=[]


def backround_image(Img):
    Width=1000
    Height=500
    global Alscreen
    Alscreen=pygame.display.set_mode( ( Width, Height) )
    Alimg=pygame.image.load("Images/"+Img+".jpg")
    Alimg2=pygame.transform.scale(Alimg,(1000,500))
    Alscreen.blit(Alimg2,(0,0))  
    
    
    #Alscreen=pygame.display.set_mode((Width,Height))
    pygame.display.update()
    
def start_listening():
    
    r=speech.Recognizer()
    with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak:")
            audio=r.listen(source)
    command=r.recognize_google(audio)
        
    print("You said: "+command)
    return command

         
"""
def speechrecog():
     r = speech.Recognizer() 
     with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
     command=r.recognize_google(audio)
     print("You said" + command)
     return command 
 """
pygame.init()


Alexa=pyttsx3.init()
Keyf='N'


#words=speechrecog()
       
       
for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_c:
                Keyf ='c'
    

#import time

       
     
       
backround_image('Cook_Bot')

while True : 
           
    try:  
          for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus="quit"
                    break
                 if EventStatus=="quit" :
                    break
                 if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_c:
                      Keyf ='c'
                    
                

          if Keyf=='c' : 
                  print("Atharva")
                  
                  #pygame.display.set_caption("Cook Bot")
                  #ALIMG=pygame.image.load("Images/Cook_Bot.jpg")
                  #Alimg2=pygame.transform.scale(ALIMG,(500,1000))
                  #Alscreen.blit(ALIMG,(0,0))
                  font=pygame.font.SysFont("Calibri (Body)",(24))
                  Text=font.render("Hello I am your interactive Bot that will make your daily eating habbits simplified",True,(255,0,0))
                  Text2=font.render("My work is to devolop a sense of healthy eating habbits and keeping track of nutritional value",True,(255,0,0))
                  Alscreen.blit(Text,(200,200))
                  Alscreen.blit(Text2,(200,400))
                  pygame.display.update()
                  
                  Alexa.setProperty('rate',120)
                  Alexa.say("Hello I am your interactive Bot that will make your daily eating habbits simplified, My work is to devolop a sense of healthy eating habbits and keeping track of nutritional value")
                  Alexa.runAndWait()
                  
                  break
         
#while True:
          if Keyf!="q":
              time.sleep(10)
              Alexa.say("Its time to have snacks!!")

    except speech.UnknownValueError:
               print("Could not understand audio")
    except speech.RequestError as e:
                print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
                break
          
          
              
                  

    
 
           
             
       
       
"""
   while True:
             pygame.display.update()
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    EventStatus="quit"
                    break
                 if EventStatus=="quit" :
                       break
    """