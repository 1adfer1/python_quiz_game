from colorama import Fore,Style
import os
from time import sleep
from random import randint, shuffle

import os

# Use the appropriate command based on the operating system
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()  # Call this function to clear the screen


# _____                   _             _   _____                          _   
#|_   _|__ _ __ _ __ ___ (_)_ __   __ _| | |  ___|__  _ __ _ __ ___   __ _| |_ 
#  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | |_ / _ \| '__| '_ ` _ \ / _` | __|
#  | |  __/ |  | | | | | | | | | | (_| | | |  _| (_) | |  | | | | | | (_| | |_ 
#  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_| |_|  \___/|_|  |_| |_| |_|\__,_|\__|

# A function used in menus to print borders/line breaks
def printBorder(border_width):
    for i in range(0,border_width):
        end = ""
        if i==border_width-1: end = "\n" 
        if i%2 == 0:
            print(Fore.LIGHTRED_EX + "=", end=end)
        else:
            print(Fore.RED + "=", end=end)




# _____ _ _        ___ ___  
#|  ___(_) | ___  |_ _/ _ \ 
#| |_  | | |/ _ \  | | | | |
#|  _| | | |  __/  | | |_| |
#|_|   |_|_|\___| |___\___/ 

# Function to read a txt quiz file **generated by CHATGPT**, and return it as a list
def readQuiz(dir):
    with open(dir,"r") as quiz_file:
        return quiz_file.readlines()

def listQuizes():
    # List directories in the current folder
    dirs = os.listdir("/Users/adfer11/Desktop/Codenation/python/learning_python/codenation_python_with_ai/week_5/quiz_game/quiz_game_python_main/quizes")

    for index, value in enumerate(dirs):
        dirs[index] = value.replace(".txt", "")

    return dirs

    



#  _   _ ___     
# | | | |_ _|___ 
# | | | || |/ __|
# | |_| || |\__ \
#  \___/|___|___/

# Menu user interface, returns the users choice
def menuUI(current_quiz):
    os.system("cls") # Clear terminal

    printBorder(33)
    print(Fore.LIGHTRED_EX + "      Quiz Game!" )
    printBorder(33)
    print(Fore.WHITE + Style.DIM + "Current quiz: " + current_quiz + Style.RESET_ALL)

    print(Fore.LIGHTRED_EX + "1." + Fore.LIGHTWHITE_EX + " Start Quiz")
    print(Fore.LIGHTRED_EX + "2." + Fore.LIGHTWHITE_EX + " Quiz Selection")
    print(Fore.LIGHTRED_EX + "3." + Fore.LIGHTWHITE_EX + " Quit")

    # Ask for the user's input
    user_input = input(Fore.LIGHTRED_EX + Style.DIM + "\n> " + Style.NORMAL)  # User input
    print(Style.RESET_ALL)
    return user_input

# Single question user interface, displays the question info, returns the users choice
def questionUI(question, options):
    os.system("cls") # Clear terminal

    printBorder(33)
    print(Fore.LIGHTRED_EX + "      Quiz Question!" )
    printBorder(33)
    
    # Display the question
    print(Fore.LIGHTWHITE_EX + question + "\n")
    
    # Display the options (assuming 'options' is a list of 4 choices)
    print(Fore.LIGHTRED_EX + "1." + Fore.LIGHTWHITE_EX + " " + options[0])
    print(Fore.LIGHTRED_EX + "2." + Fore.LIGHTWHITE_EX + " " + options[1])
    print(Fore.LIGHTRED_EX + "3." + Fore.LIGHTWHITE_EX + " " + options[2])
    print(Fore.LIGHTRED_EX + "4." + Fore.LIGHTWHITE_EX + " " + options[3])
    
    # Ask for the user's input
    user_input = input(Fore.LIGHTRED_EX + Style.DIM + "\nSelect your answer (1-4): " + Style.NORMAL)
    print(Style.RESET_ALL)
    
    return user_input

# Displays the users final score
def finalScoreUI(score, max_score):
    os.system("cls") # Clear terminal

    printBorder(33)
    print(Fore.LIGHTRED_EX + "      The Results!" )
    printBorder(33)
    
    # Diaplys score
    print(Fore.LIGHTRED_EX + "> " + Fore.LIGHTWHITE_EX + f"You got {score} out of {max_score}")
    
    # Ask for the user's input, to stall
    input(Fore.LIGHTRED_EX + Style.DIM + "\n Hit enter to continue" + Style.NORMAL)
    print(Style.RESET_ALL)

def quizSelectionUI(quizes, cur_quiz):
    os.system("cls")

    printBorder(33)
    print(Fore.LIGHTRED_EX + f"           Select you quiz!" )
    printBorder(33)
    print(Fore.WHITE + Style.DIM + "Current quiz: " + cur_quiz + Style.RESET_ALL)

    # Display the quizes
    count = 1
    for quiz in quizes:
        print(Fore.LIGHTRED_EX + str(count) + "." + Fore.LIGHTWHITE_EX + " " + quiz)
        count += 1
    print(Fore.LIGHTRED_EX + str(count) + "." + Fore.LIGHTWHITE_EX + " << Back")

    user_input = input(Fore.LIGHTRED_EX + Style.DIM + "\n Enter quiz number: " + Style.NORMAL)
    print(Style.RESET_ALL)

    return user_input


#  _                          
# | |    ___   ___  _ __  ___ 
# | |   / _ \ / _ \| '_ \/ __|
# | |__| (_) | (_) | |_) \__ \
# |_____\___/ \___/| .__/|___/
#                  |_|                  ** Human / Chat GPT Commented**


# Function to handle a single question and get the user's input
def questionLoop(question_info):

    # Extract the question, correct answer, and the multiple choice options
    question = question_info[0]
    right_answer = question_info[1]
    mutliple_choice = question_info[2:6]
    
    valid_answer = False 
    while valid_answer != True:  # Keep asking until a valid answer (1, 2, 3, or 4) is given
        
        # Display the question and options to the user, collect their input
        user_input = questionUI(question, mutliple_choice)
        
        
        if user_input in ["1", "2", "3", "4"]: # Valid, Exit the loop
            valid_answer = True  
        else: # Invalid, Inform user
            print(Fore.LIGHTWHITE_EX + Style.DIM + "\n> Incorrect answer, please enter 1, 2, 3 or 4." + Style.RESET_ALL)
            sleep(1)


    # Check if the user's answer matches the correct answer
    if right_answer == user_input:
        return True
    return False


# Function to loop through all the questions in the quiz
def quizLoop(cur_quiz):

    quiz = readQuiz(os.path.join("/Users/adfer11/Desktop/Codenation/python/learning_python/codenation_python_with_ai/week_5/quiz_game/quiz_game_python_main/quizes", cur_quiz + ".txt"))
    shuffle(quiz)

    correct_count = 0  # Initialize the count of correct answers

    # Loop through each question in the quiz
    for question in quiz:
        answer = questionLoop(question.split("|"))
        if answer == True:
            correct_count += 1
    
    # Calculate the score: +5 points for each correct answer, -2 for incorrect ones
    score = (correct_count * 5) + ((len(quiz) - correct_count) * -2)
    
    # If the score is negative, set it to 0 (no negative scores allowed)
    if score < 0:
        score = 0

    # Display final scores
    finalScoreUI(score, len(quiz) * 5)

# Displays quiz files to user, and retunrs their input
def quizSelectionLoop(cur_quiz):
    quiz_list = listQuizes() 

    valid_exit = False 
    while valid_exit != True: # Loop till user exit
        user_input = quizSelectionUI(quiz_list, cur_quiz)
        if (int(user_input) > 0 and int(user_input) <= len(quiz_list)): # Valid quiz
            cur_quiz = quiz_list[int(user_input)-1]  # Change current quiz to entry

        elif (int(user_input) == len(quiz_list)+1): # Exit
            valid_exit = True

        else: # Invalid input
            print(Fore.LIGHTWHITE_EX + Style.DIM + "\n> Incorrect entry, try again." + Style.RESET_ALL)
            sleep(1)   
            
    return cur_quiz



def mainMenuLoop():
    os.system("cls")

    cur_quiz = listQuizes()[0]

    exit = False 
    while exit != True: # Loop until exit
        user_input = menuUI(cur_quiz)

        if (user_input == "3"): # Quit Game
            exit = True

        elif (user_input == "2"):
            cur_quiz = quizSelectionLoop(cur_quiz)

        elif (user_input == "1"): # Start  Quiz
            quizLoop(cur_quiz)


mainMenuLoop()


# To generate a new quiz, user this prompt


#I want you to give me a list of CHANGEME questions on CHANGEME. But it in a text file. I want each line to look like this [Question]|[Answer (1,2,3,4)]|[Multiple Choice 1]|[Multiple Choice 2]|[Multiple Choice 3]|[Multiple Choice 4]