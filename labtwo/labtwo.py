import pygame
from pygame.locals import *
import sys
import random
import webbrowser

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
SILVER = (132,132,132)

pscore = 0
cscore = 0


def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def computer_choice():
    computerChoice = random.choice(choices)
    return computerChoice

def machine_comp(playerChoice,computerChoice):
    rbeats = ["Scissors","Lizard"]
    pbeats = ["Rock","Spock"]
    scbeats = ["Paper","Lizard"]
    lbeats = ["Spock","Paper"]
    spbeats = ["Rock","Scissors"]

    if playerChoice != computerChoice:

        if (playerChoice == "Rock") and (computerChoice == rbeats[0] or computerChoice == rbeats[1]):
            winner = "Player wins: Rock defeats %s" % (computerChoice)
            won = "Player"
            score_update(won)
            return winner
        
        elif (playerChoice == "Paper") and (computerChoice == pbeats[0] or computerChoice == pbeats[1]):
            winner = "Player wins: Paper defeats %s" % (computerChoice)
            won = "Player"
            score_update(won)
            return winner

        elif (playerChoice == "Scissors") and (computerChoice == scbeats[0] or computerChoice == scbeats[1]):
            winner = "Player wins: Scissors defeats %s" % (computerChoice)
            won = "Player"
            score_update(won)
            return winner

        elif (playerChoice == "Lizard") and (computerChoice == lbeats[0] or computerChoice == lbeats[1]):
            winner = "Player wins: Lizard defeats %s" % (computerChoice)
            won = "Player"
            score_update(won)
            return winner
        elif (playerChoice == "Spock") and (computerChoice == spbeats[0] or computerChoice == spbeats[1]):
            winner = "Player wins: Spock defeats %s" % (computerChoice)
            won = "Player"
            score_update(won)
            return winner

       #####################################    Computer Wins           #################################
       
        elif (computerChoice == "Rock") and (playerChoice == rbeats[0] or playerChoice == rbeats[1]):
            winner = "Computer wins: rock defeats %s" % (playerChoice)
            won = "Computer"
            score_update(won)
            return winner

        elif (computerChoice == "Paper") and (playerChoice == pbeats[0] or playerChoice == pbeats[1]):
            winner = "Computer wins: paper defeats %s" % (playerChoice)
            won = "Computer"
            score_update(won)
            return winner

        elif (computerChoice == "Scissors") and (playerChoice == scbeats[0] or playerChoice == scbeats[1]):
            winner = "Computer wins: scissors defeats %s" % (playerChoice)
            won = "Computer"
            score_update(won)
            return winner

        elif (computerChoice == "Lizard") and (playerChoice == lbeats[0] or playerChoice == lbeats[1]):
            winner = "Computer wins: lizard defeats %s" % (playerChoice)
            won = "Computer"
            score_update(won)
            return winner

        elif (computerChoice == "Spock") and (playerChoice == spbeats[0] or playerChoice == spbeats[1]):
            winner = "Computer wins: spock defeats %s" % (playerChoice)
            won = "Computer"
            score_update(won)
            return winner

        else:
            pass

    else:
        winner = "Tie! Try Again."
        return winner
    

def score_update(won):
    global pscore
    global cscore
    if won == "Player":
        pscore += 1
        print pscore
    elif won == "Computer":
        cscore += 1
        print cscore
    else: 
        pass

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

    #image loads:
    rock = pygame.image.load("rock.png")
    paper = pygame.image.load("paper.png")
    scissors = pygame.image.load("scissors.png")
    lizard = pygame.image.load("lizard.png")
    spock = pygame.image.load("spock.png")

    run = True 
   
    playerChoice = ""
    computerChoice = ""
    
    choices = ["Rock","Paper","Scissors","Lizard","Spock"]
    
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
                background.fill(WHITE)
                atom = pygame.image.load("atom.png")
                menuText1 = menufont.render("ROCK, PAPER,", True, BLACK)
                menuText2 = menufont.render("SCISSORS,", True, BANGRED)
                menuText3 = menufont.render("LIZARD, SPOCK?", True, BLACK)
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

                elif 534 + 70 > mouse[0] > 534 and 286 + 70 > mouse[1] > 286 and mouseclick:
                    playerChoice = choices[2]
                
                elif 497 + 70 > mouse[0] > 497 and 425 + 70 > mouse[1] > 425 and mouseclick:
                    playerChoice = choices[1]
                
                elif 311 + 70 > mouse[0] > 311 and 287 + 70 > mouse[1] > 287 and mouseclick:
                    playerChoice = choices[3]

                elif 347 + 70 > mouse[0] > 347 and 423 + 70 > mouse[1] > 423 and mouseclick:
                    playerChoice = choices[0]
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
                            computerChoice = computer_choice()
                            winner = machine_comp(playerChoice,computerChoice)
                    else:    
                        cont = pygame.draw.rect(background, GREEN,(700,620,120,50))

                    textSurf, textRect = text_objects("Submit!", smallText)
                    textRect.center = ((700+(120/2)), (620+(50/2)))
                    background.blit(textSurf, textRect)
                else: 
                    pass
                
            if Background == 3:
                background.fill(WHITE)

                pselect = menufont.render("Player: %s" % (pscore), True, BANGRED)
                
                if playerChoice == choices[0]:
                    background.blit(rock, (330,70))
                elif playerChoice == choices[1]:
                    background.blit(paper, (330,70))
                elif playerChoice == choices[2]:
                    background.blit(scissors,(330,70))
                elif playerChoice == choices[3]:
                    background.blit(lizard, (330,70))
                elif playerChoice == choices[4]:
                    background.blit(spock, (330,70))
                
                vs = menufont.render("VS", True, BLACK)
                
                cselect = menufont.render("Computer: %s" % (cscore), True, BANGRED)
                
                if computerChoice == choices[0]:
                    background.blit(rock, (330,435))
                elif computerChoice == choices[1]:
                    background.blit(paper, (330,435))
                elif computerChoice == choices[2]:
                    background.blit(scissors, (330,435))
                elif computerChoice == choices[3]:
                    background.blit(lizard, (330,435))
                elif computerChoice == choices[4]:
                    background.blit(spock, (330,435))
                else:
                    pass
                
                wintext = smallText.render(winner, True, BLACK)

                if 10 + 100 > mouse[0] > 10 and 10 + 50 > mouse[1] > 10:
                    cont = pygame.draw.rect(background, BRIGHT_RED,(10,10,120,50))
                    if mouseclick:
                        playerChoice = ""
                        computerChoice = ""
                        Background = 1
                else:    
                    cont = pygame.draw.rect(background, BANGRED,(10,10,120,50))

                textSurf, textRect = text_objects("Again!", smallText)
                textRect.center = ((10+(120/2)), (10+(50/2)))
                background.blit(textSurf, textRect)

                if 770 + 100 > mouse[0] > 770 and 10 + 50 > mouse[1] > 10:
                    cont = pygame.draw.rect(background, SILVER,(770,10,120,50))
                    if mouseclick:
                        Background = 4
                else:    
                    cont = pygame.draw.rect(background, BLACK,(770,10,120,50))

                textSurf, textRect = text_objects("Quit!", smallText)
                textRect.center = ((770+(120/2)), (10+(50/2)))
                background.blit(textSurf, textRect)


                background.blit(pselect,(330,(-25)))
                background.blit(vs,(410,(H/3+40)))
                background.blit(cselect,(260,340))

                
                if winner != "Tie! Try Again.": 
                    background.blit(wintext,(240,660))
                else:         
                    background.blit(wintext,(320,660))

            if Background == 4:
                background.fill(WHITE)

                byeText = menufont.render("Thank you for playing!",True,BLACK)
                byeText2 = menufont.render("Come again soon!",True,BLACK)

                likeText = smallText.render('Click if you liked it!', True, BANGRED)
                likeicon = pygame.image.load("like.png")

                background.blit(byeText,(130,10))
                background.blit(likeText,(340,250))
                background.blit(likeicon,(350,290))
                background.blit(byeText2,(180,580))

                if 400 + 100 > mouse[0] > 400 and 520 + 50 > mouse[1] > 520:
                    begin = pygame.draw.rect(background, BRIGHT_RED,(400,520,100,50))
                    if mouseclick:
                        Background += 1
                else:
                    begin = pygame.draw.rect(background, BANGRED,(400,520,100,50))

                textSurf, textRect = text_objects("Quit!", smallText)
                textRect.center = ((400+(100/2)), (520+(50/2)))
                background.blit(textSurf, textRect)

                if 350 +  204 > mouse[0] > 290 and 290 + 204 > mouse[1] > 290 and mouseclick:
                    webbrowser.open("heronnavarro.wordpess.com", new = 1)

        pygame.display.flip()








    pygame.quit()
    quit()