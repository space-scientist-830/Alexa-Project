import pygame
pygame.init()

Width=1280
Height=720

screen=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("PSLV C25 Launch")
screenIMG=pygame.image.load("Images/Atharva.jpg")

screen.blit(screenIMG,(0,0))
EventStatus=("None")

while True:
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   EventStatus="quit"
                   break
           if EventStatus=="quit" :
             break