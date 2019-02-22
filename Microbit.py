from microbit import *


while True:
       import random
player_choice = 0 
if button_a.get_presses(): 
    player_choice = 1
if button_b.get_presses(): 
    player_choice = 2
if button_a.get_presses() and button_b.get_presses()
    player_choice = 3

#intro 
    print ("lets play rock, paper, scissors!")
    print (" pick rock or paper or scissors")
    player_choice = input ()


computer = random.randint (1,3) 
if player_choice == 1 and computer == 1:
    display.show (Image.CONFUSED)
if player_choice == 1 and computer == 2:
   display.show (Image.SAD)
if player_choice == 1 and computer == 3:
    display.show (Image.SMILE)


if player_choice == 2 and computer == 1:
    display.show (Image.SMILE)
if player_choice == 2 and computer == 2:
    display.show (Image.CONFUSED)
if player_choice == 2 and computer == 3:  
    display.show (Image.SAD)

if player_choice == 3 and computer == 1:
    display.show (Image.SAD)
if player_choice == 3 and computer == 2:
    display.show (Image.SMILE)
if player_choice == 3 and computer == 3:
    display.show (Image.CONFUSED)




if button_a.get_presses(): 
    if button_a.get_presses(): 
        break

if button_b.get_presses(): 
    if button_b.get_presses(): 
    break 
