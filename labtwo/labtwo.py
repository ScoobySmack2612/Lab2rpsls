import pygame
from pygame.locals import *
import sys
import random
import webbrowser
import os.path

W = 900
H = 650
BLACK = (0,0,0)
WHITE = (255,255,255)
BANGRED = (150,0,0)
RED = (210,0,0)
BRIGHT_RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,210,20)
BRIGHT_GREEN= (20,255,0)
SILVER = (132,132,132)

Background = 1

pscore = 0
cscore = 0


def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button(x,y,w,h,ic,ac,text,textstyle,action):
    global Background
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        begin = pygame.draw.rect(background, ac,(x,y,w,h))
        if action == "increment" and mouseclick:
            Background +=1
        elif action == "quit" and mouseclick:
            url = "http://heronnavarro.wordpress.com"    
            webbrowser.get().open(url)
            pygame.QUIT
            quit()
        elif action == "repeat" and mouseclick:
            Background = 1
            
    else:
        begin = pygame.draw.rect(background, ic,(x,y,w,h))

    textSurf, textRect = text_objects(text, textstyle)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    background.blit(textSurf, textRect)

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
    elif won == "Computer":
        cscore += 1
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
    bigtext = pygame.font.SysFont("lilypuc",50,True)
    gamefont = pygame.font.SysFont("Papyrus", 40, True)
    fineprint = pygame.font.SysFont("Papyrus",20,True)


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
                playerChoice = ""
                background.fill(WHITE)
                atom = pygame.image.load("atom.png")
                menuText1 = menufont.render("ROCK, PAPER,", True, BLACK)
                menuText2 = menufont.render("SCISSORS,", True, BANGRED)
                menuText3 = menufont.render("LIZARD, SPOCK?", True, BLACK)
                background.blit(atom,(440,0))
                background.blit(menuText1, [W/2-240,60])
                background.blit(menuText2, [W/2-180,125])
                background.blit(menuText3,[W/2-300,190])

                gobtn = button(400,450,100,50,BANGRED,BRIGHT_RED,"BEGIN",smallText,"increment")
                
            
            if Background == 2:
                background.fill(WHITE)
                selection = pygame.image.load("rpsls.jpg")
                selectText = menufont.render("MAKE YOUR", True, BLACK)
                selectText2 = menufont.render("SELECTION", True, BANGRED) 
                
                

                background.blit(selection,(210,180))
                background.blit(selectText, (220,75))
                background.blit(selectText2, (230,525))


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

                    if 90 + 120 > mouse[0] > 90 and 300 + 50 > mouse[1] > 300:
                        cont = pygame.draw.rect(background, BRIGHT_GREEN,(90,300,120,50))
                        if mouseclick:
                            Background += 1
                            computerChoice = computer_choice()
                            winner = machine_comp(playerChoice,computerChoice)
                    else:    
                        cont = pygame.draw.rect(background, GREEN,(90,300,120,50))

                    textSurf, textRect = text_objects("Submit!", smallText)
                    textRect.center = ((90+(120/2)), (300+(50/2)))
                    background.blit(textSurf, textRect)
                
            if Background == 3:
                background.fill(WHITE)

                pselect = bigtext.render("Player: %s" % (pscore), True, BANGRED)
                
                if playerChoice == choices[0]:
                    background.blit(rock, (70,150))
                elif playerChoice == choices[1]:
                    background.blit(paper, (70,150))
                elif playerChoice == choices[2]:
                    background.blit(scissors,(70,150))
                elif playerChoice == choices[3]:
                    background.blit(lizard, (70,150))
                elif playerChoice == choices[4]:
                    background.blit(spock, (70,150))
                
                vs = menufont.render("VS", True, BLACK)
                
                cselect = bigtext.render("Computer: %s" % (cscore), True, BANGRED)
                
                if computerChoice == choices[0]:
                    background.blit(rock, (590,150))
                elif computerChoice == choices[1]:
                    background.blit(paper, (590,150))
                elif computerChoice == choices[2]:
                    background.blit(scissors, (590,150))
                elif computerChoice == choices[3]:
                    background.blit(lizard, (590,150))
                elif computerChoice == choices[4]:
                    background.blit(spock, (590,150))
                else:
                    pass
                
                wintext = smallText.render(winner, True, BLACK)

                repeatbtn = button(10,10,100,50,BANGRED,BRIGHT_RED,"AGAIN!",smallText,"repeat")
                quitbtn = button(770,10,100,50,BLACK,SILVER,"QUIT!",smallText,"increment")


                background.blit(pselect,(80,500))
                background.blit(vs,(390,(H/3+50)))
                background.blit(cselect,(600,500))

                
                if winner != "Tie! Try Again.": 
                    background.blit(wintext,(220,50))
                else:         
                    background.blit(wintext,(350,50))

            if Background == 4:
                background.fill(WHITE)

                byeText = menufont.render("Thank you for playing!",True,BLACK)
                byeText2 = menufont.render("Come again soon!",True,BLACK)

                likeText = smallText.render('Click below if you liked it!', True, BANGRED)
                likeicon = pygame.image.load("like.png")

                background.blit(byeText,(5,10))
                background.blit(likeText,(300,150))
                background.blit(likeicon,(350,200))
                background.blit(byeText2,(110,550))

                endbtn = button(400,450,100,50,BLACK,SILVER,"QUIT",smallText,"quit")

                #url to wordpress
                url = "http://heronnavarro.wordpress.com"

                if 350 + 204 > mouse[0] > 350 and 200 + 204 > mouse[1] > 200 and mouseclick:
                    webbrowser.get().open(url)

        pygame.display.flip()

        








    pygame.quit()
    quit()