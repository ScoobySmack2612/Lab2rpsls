import pygame
from pygame.locals import *

W = 900
H = 700
BLACK = (0,0,0)
WHITE = (255,255,255)
BANGRED = (150,0,0)
RED = (210,0,0)
BRIGHT_RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,210,20)
BRIGHT_GREEN= (20,255,0)

def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

if __name__ == "__main__":
    pygame.init()
    size = (W,H)
    window = pygame.display.set_mode(size)
    title = pygame.display.set_caption("Let's Play RPSLS...")

    background = pygame.display.get_surface()
    background = pygame.display.set_mode(size)
    background.fill(WHITE)

    clock = pygame.time.Clock()
    clock.tick(60)

    smallText = pygame.font.Font("freesansbold.ttf",25)
    menufont = pygame.font.SysFont("lilyupc", 100, True) 
    gamefont = pygame.font.SysFont("Papyrus", 40, True)
    fineprint = pygame.font.SysFont("Papyrus",20,True)

    Background = 1


    run = True 
   
    playerChoice = ""
    computerChoice = ""
    choices = ["Rock","Paper","Scissors","Lizzard","Spock"]
    
    while run:
        
        
        


        events = pygame.event.get()
        
        mouse = pygame.mouse.get_pos()
        mouseclick = False
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouseclick = True

            if Background == 1:
                atom = pygame.image.load("atom.png")
                menuText1 = menufont.render("ROCK, PAPER,", True, BLACK)
                menuText2 = menufont.render("SCISSORS,", True, BANGRED)
                menuText3 = menufont.render("LIZZARD, SPOCK?", True, BLACK)
                background.blit(atom,(440,0))
                background.blit(menuText1, [W/2-240,60])
                background.blit(menuText2, [W/2-180,125])
                background.blit(menuText3,[W/2-300,190])


                

                if 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450:
                    begin = pygame.draw.rect(background, BRIGHT_RED,(400,450,100,50))
                    if mouseclick:
                        Background += 1
                else:
                    begin = pygame.draw.rect(background, BANGRED,(400,450,100,50))

                
                textSurf, textRect = text_objects("BEGIN!", smallText)
                textRect.center = ((400+(100/2)), (450+(50/2)))
                background.blit(textSurf, textRect)
            
            if Background == 2:
                background.fill(WHITE)
                selection = pygame.image.load("rpsls.jpg")
                selectText = menufont.render("MAKE YOUR", True, BLACK)
                selectText2 = menufont.render("SELECTION", True, BANGRED) 
                
                

                background.blit(selection,(210,180))
                background.blit(selectText, (250,75))
                background.blit(selectText2, (270,525))


                if 418 + 70 > mouse[0] > 418 and 205 + 70 > mouse[1] > 205 and mouseclick:
                    playerChoice = choices[4]
                    print "%s Clicked" % (playerChoice)

                elif 534 + 70 > mouse[0] > 534 and 286 + 70 > mouse[1] > 286 and mouseclick:
                    playerChoice = choices[2]
                    print "%s Clicked" % (playerChoice)
                
                elif 497 + 70 > mouse[0] > 497 and 425 + 70 > mouse[1] > 425 and mouseclick:
                    playerChoice = choices[1]
                    print "%s Clicked" % (playerChoice)
                
                elif 311 + 70 > mouse[0] > 311 and 287 + 70 > mouse[1] > 287 and mouseclick:
                    playerChoice = choices[3]
                    print "%s Clicked" % (playerChoice)

                elif 347 + 70 > mouse[0] > 347 and 423 + 70 > mouse[1] > 423 and mouseclick:
                    playerChoice = choices[0]
                    print "%s Clicked" % (playerChoice)
                else: 
                    pass

                

                if playerChoice != "":
                    pchoiceText = gamefont.render("Your Choice:", True, BANGRED)
                    pchoiceText2 = gamefont.render(playerChoice, True, BANGRED)
                    checkText = fineprint.render("You make reselect before continuing.", True, BLACK)

                    background.blit(pchoiceText,(20,200))
                    background.blit(pchoiceText2,(220,200))
                    background.blit(checkText, (20,250))

                    if 700 + 100 > mouse[0] > 700 and 620 + 50 > mouse[1] > 620:
                        cont = pygame.draw.rect(background, BRIGHT_GREEN,(700,620,120,50))
                        if mouseclick:
                            Background += 1
                    else:    
                        cont = pygame.draw.rect(background, GREEN,(700,620,120,50))

                    textSurf, textRect = text_objects("Submit!", smallText)
                    textRect.center = ((700+(120/2)), (620+(50/2)))
                    background.blit(textSurf, textRect)
                else: 
                    pass

            if Background == 3:
                background.fill(WHITE)

                vs = menufont.render("VS", True, BLACK)

                background.blit(vs,(W/2-30,H/2-50))               





        pygame.display.flip()








    pygame.quit()
    quit()