#Import Statements
import sys, os
from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
import pprint
from examples import custom_style_2
from pyfiglet import Figlet
import PySimpleGUI as sg
from termcolor import colored



#Main Definition - constants
menu_actions = {}

#=======================
#     Menus Functions
#=======================

#Main Menu

#Format Title
def log(string,color,font="slant",figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string,color))
        else:
            six.print_(colored(figlet_format (
                string,font=font),color
            ))
    else:
        six.print_(string)

#Options to go back to main menu
backOption = [
    {
        'type':'list',
        'name':'backOptions',
        'message':'Options',
        'choices': [
            'Main Menu',
            'Quit'
        ]
    }
]

#Main Menu Function
def main_menu():
    
    #Clear Screen
    os.system('cls')

    #Menu Options
    questions = [
        {
        'type':'list',
        'name':'menu',
        'message':'Please make a choice from the list below',
        'choices': [
            'First Time User',
            'Track Workout Data',
            'Analyze Previous Workout Data'
            ]
        }
    ]

    #Font type of title
    f = Figlet(font='slant')
    print(f.renderText('Workout Tracker'))

    #Print out Questions menu
    answers = prompt(questions, style=custom_style_2)

    #Process Menu Choice
    if answers['menu'] == 'First Time User':
        newUser()
    if answers['menu'] == 'Track Workout Data':
        workoutData()
    if answers['menu'] == 'Analyze Previous Workout Data':
        analyzeData()

    print_json(answers)

#New User Menu Choice
def newUser():
    #Clear screen
    os.system('cls')

    #Call workout python file
    from firstTimeUserDriver import main

    #Print out menu following data
    print('\n')
    answers = prompt(backOption,style=custom_style_2)

    if answers['backOptions']=='Main Menu':
        back
    if answers['backOptions']=='Quit':
        exit()

    return


#Workout Menu Choice
def workoutData():
    #Clear screen
    os.system('cls')

    #Call workout python file
    from workoutmain import main

    #Print out menu following data
    print('\n')
    answers = prompt(backOption,style=custom_style_2)

    if answers['backOptions']=='Main Menu':
        back
    if answers['backOptions']=='Quit':
        exit()

    return


#Back to main menu
def back():
    menu_actions['main_manu']()

#Exit
def exit():
    print("Keep on grinding!")
    sys.exit()


#====================
#   Menu Definitions
#====================

#Menu
menu_actions = {
    'main_menu': main_menu,
    '1': newUser,
    '2': workoutData,
    '9':back,
    '0':exit,
}

#====================
#  MAIN PROGRAM
#====================

#Main Program
if __name__ == "__main__":
    #Launch Main Menu
    main_menu()