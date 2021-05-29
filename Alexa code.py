
import pygame,sys
import pyttsx3
import time
import speech_recognition as speech
from datetime import datetime
from pynput import keyboard
keyn="e"

Alexa="engine"
Text="formula"


EventStatus='None'
Alscreen=[]
Alimg=[]
coordinates='none'


def display_text_on_screen(Alexa,coordinatesx,coordinatesy):
   global Text
   font=pygame.font.SysFont("Calibri (Body)",36)
   Text=font.render(Alexa,True,(255,0,0))
   Alscreen.blit(Text,(coordinatesx,coordinatesy))
   
   pygame.display.update()
   
Keyf='none'
   
                 
                 

def backround_image(Img):
    print("1.....")
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
        
    return command
    

Alexa=pyttsx3.init()    
#Keym="init"     
 

pygame.init()


Alexa=pyttsx3.init()
Keyf='N'
#Keym="init"


#words=speechrecog()
    
"""      
for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                Keyf ='c'
    """

#import time

       
     
       
  
backround_image('Cook_Bot')


def on_press(key):
    try:
        global Keyf
        Keyf={0}.format(
            key.char)
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    print('The key that was pressed is: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

while True : 
           
    #try:  
          for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    EventStatus="quit"
                    break
                 if EventStatus=="quit" :
                    break
                 """
                 if event.type==pygame.KEYDOWN:
                  print("key="+str(event.key))
                  if event.key==pygame.K_c:
                      Keyf ='c'
                  if event.key==pygame.K_q:
                      Keym='q'
                      
                      break
          
             """         
                    
                

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
                  #event = None
                  
                  
                #  backround_image("Cook_Bot (5)")
                 # start_listening()
                  
                  #break
   
    
          if Keyf=='q' :
                       hour=0
                       miniute=0

                       now=datetime.now()
                       current_time=now.strftime("%H:%M")
                       backround_image("Image for asking to give time fpor setting reminders")
                       display_text_on_screen(current_time,200,200)
              
                       #Alscreen.blit(Text,(200,200))
                       pygame.display.update()
              
                       hour=start_listening()
                       print("hour="+hour)
                       miniute=start_listening()
                       print("miniute="+miniute)
                       display_text_on_screen(hour+":"+miniute,400,200)
                       pygame.display.update()
                      # miniute=start_listening()
                       #display_text_on_screen(miniute,450,200)
                       #Alscreen.blit(Text,(400,200))
                       #pygame.display.update()
                      # miniute=start_listening()
                       #print(miniute)
                      # display_text_on_screen(miniute)
                      # Alscreen.blit(Text,(400,250))
                      # pygame.display.update()
                       while True:
                           now=datetime.now()
                           current_hour=now.strftime("%H")
                           current_miniute=now.strftime("%M")

                       #display_text_on_screen(current_hour,305,200)
                       print(current_hour)
                       #Alscreen.blit(Text,(305,200))
                      # pygame.display.update()
                       #display_text_on_screen(current_miniute,305,200)
                       print(current_miniute)
                       #$Alscreen.blit(Text,(305,200))
                       #pygame.display.update()
                       time.sleep(1)
    
                       if current_hour==hour and current_miniute==miniute :
                           Alexa.say("Its time to drink water")
                           Alexa.runAndWait()
                           if Keyf=="e" :
                               break
                          # break   
                    
 
pygame.quit()
sys.exit()
    
                
   

             
       
    
