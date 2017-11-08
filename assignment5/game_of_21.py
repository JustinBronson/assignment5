#Created by: Justin Bronson
#Created on: Nov 2017
#Created for ICS3U
#This program is a virtual game of 21

import ui
from numpy import random

def start_game():	
    userCardOne = random.randint(1,11)
    userCardTwo = random.randint(1,11)
    
    view['compCardOne_label'].text = ' '
    view['compCardTwo_label'].text = ' '
    view['compCardThree_label'].text = ' '
    
    view['answer_label'].text = ' '
    view['userCardSum_label'].text = ' '
    view['compCardSum_label'].text = ' '
    
    view['userCardOne_label'].text = str(userCardOne)
    view['userCardTwo_label'].text = str(userCardTwo)
    view['userCardThree_label'].text = ' '
    
    #to do disable play again button
    view['play_again_button'].enabled = False
    
    #to do enable extra card and check buttons
    view['extra_button'].enabled = True
    view['check_button'].enabled = True

def check_button_touch_up_inside(sender):
    calculate_winner(False)	

def extra_button_touch_up_inside(sender):
    calculate_winner(True)	
	
def play_again_button_touch_up_inside(sender):
    start_game()
	
def calculate_winner(extraCard):
    #to do disable play again button
    view['play_again_button'].enabled = True
    
    #to do enable extra card and check buttons
    view['extra_button'].enabled = False
    view['check_button'].enabled = False
    
    userCardOne = int(view['userCardOne_label'].text)
    userCardTwo = int(view['userCardTwo_label'].text)
    
    #to do extra card logic
    if extraCard == True:
        userCardThree = random.randint(1,11)
        view['userCardThree_label'].text = str(userCardThree)
    else:
        userCardThree = 0
    
    compCardOne = random.randint(1,11)
    compCardTwo = random.randint(1,11)
    compCardThree = random.randint(1,11)
    
    
    compCardSum = compCardOne + compCardTwo + compCardThree
    userCardSum = userCardOne + userCardTwo + userCardThree
    
    view['compCardOne_label'].text = str(compCardOne)
    view['compCardTwo_label'].text = str(compCardTwo)
    view['compCardThree_label'].text = str(compCardThree)
    
    view['compCardSum_label'].text = 'Computer score: ' + str(compCardSum)
    view['userCardSum_label'].text = 'Your score: ' + str(userCardSum)
    
    if compCardSum > 21 or userCardSum > 21:
        if compCardSum > 21 and userCardSum > 21:
            view['answer_label'].text = 'You tied'
        elif compCardSum > 21:
            view['answer_label'].text = 'You win'
        else:
            view['answer_label'].text = 'You lose'
    elif userCardSum == compCardSum:
        view['answer_label'].text = 'You tied'
    elif userCardSum > compCardSum:
        view['answer_label'].text = 'You win'
    else:
        view['answer_label'].text = 'You lose'

view = ui.load_view()
start_game()
view.present('sheet')
