# Questions/Quizzes -->

# Level 1 (Easy)

easy = """The _____1_____ are called the Ships of the Desert.
They are used to _____2_____ people and loads from one place to another.
They have a huge _____3_____ on their body where they store their fat.
They can live without _____4_____ for many days.
Their thick fur helps them to stop the sunshine from warming their bodies.
Camels have long necks and long legs. They have two toes on each foot.
They can move very _____5_____ on sand. They eat plants, grasses and bushes.
They do not harm anyone. Some of the camels have _____6_____ humps. These camels are called _____7_____ camels.\n\n"""

# Level 2 (Medium)

medium = """There is a _____1_____ in front of my house.
There are many plants and trees in it.
There bloom flowers of many colours in _____2_____.
Their _____3_____ spreads all around. In the evening, the garden is filled with men, women and children.
People _____4_____ here and there and enjoy themselves.
Children run _____5_____ in the garden.
Now they are here and at the next moment, they are in the other _____6_____ of the garden.
I also go to the garden for a walk on every evening.
Many _____7_____ look after the garden.\n\n"""

# Level 3 (Hard)

hard = """Personal _____1_____ is mostly a public matter; we allow all kinds of invasions of personal space in _____2_____.
The _____3_____ of it vary according to geography.
People who live in Calcutta have less personal space as compared to the _____4_____ of Colorado.
"Don't tread on me" could have been _____5_____ only by someone with a spread.
I would _____6_____ that people in the Northen Hemisphere have roomier _____7_____ of personal space than those in the Southern.\n\n"""


# Answers
answer_easy = ["CAMELS", "CARRY", "HUMP", "WATER", "QUICKLY", "TWO", "BACTRIAN"]
answer_medium = ["GARDEN", "SPRING", "FRAGRANCE", "WANDER", "AROUND", "CORNER", "GARDENERS"]
answer_hard = ["SPACE", "PRIVATE", "LOGISTICS", "FOLKS", "COINED", "WAGER", "CONCEPTIONS"]


# A variable specifying all the blank spaces in the quizzes
blank_spaces = ["_____1_____", "_____2_____", "_____3_____", "_____4_____", "_____5_____", "_____6_____", "_____7_____"]


def level_select():

    # "print" statements showing the available choices
    print ("Please select a game difficulty by typing it in.")
    print ("Choose a level from the following :-\n")
    print ("1. Easy")
    print ("2. Medium")
    print ("3. Hard\n")


    # A list "level_list" storing all the possible levels
    level_list = ["easy", "medium", "hard"]

    # A variable "lev" storing the entered level
    lev = raw_input("Enter Level: ").lower()
    
    while lev not in level_list:
        print str(lev).upper() + (" is not a possible option! "
                                  "Please select either Easy, Medium or Hard, Thank You!\n")
        lev = raw_input("Pick Easy, Medium, or Hard: ").lower()

    else:
        print ("You have chosen the ") + str(lev).upper() + (" Level!")
        return lev

level = level_select()
print ("\nWelcome To MadLibs!\n")

# "print" statements asking for the number of guesses a user wants to attempt all the blank
print ("\nPlease select how many guesses you want to have before the game is over.")
number_of_guess = input("Please enter a positive integer equal to or greater than 1: ")    # A variable "number_guesses" storing the number of guesses
                                                                                           #input by the user

def no_guess(number_of_guess):
    # Checks whether the no. of guesses are correct(>0)
    
    while number_of_guess <= 0:
        
            if number_of_guess == 0:
                    print  ("You need at least one guess!")
                    number_of_guess = input("Please Enter Again: ")

            elif number_of_guess < 0:
                    print ("You need to enter a number equal to 1 or greater than 1")
                    number_of_guess = input("Please Enter Again: ")

    # Prints the number of guesses entered by user
    print ("You've chosen to have ") + str(number_of_guess) + (" guess(s) per question")

num_of_guess = no_guess(number_of_guess)

print ("\nThe current paragraph reads as such: \n")


def correct_guess(guess, list_answer_element):
    # Comment --> USE OF FUNCTION
    """ This function checks whether the guess is correct and returns it only if it's correct.
        An input "guess" is taken from the user and an element of the list of correct answers for the quiz(given) and passed as arguements
        and returns the guess if it's correct, else, it return nothing. """
    
    if guess == list_answer_element:
        return guess
    else:
        return None
        

def quiz_select(level):
    # Comment --> USE OF FUNCTION
    """ This function takes the level selected by the user as the arguement and
        outputs, which quiz to select. """
    
    if level == "easy": 
        return easy
    if level == "medium":
        return medium
    if level == "hard":
        return hard


def answers_select(level):
    # Comment --> USE OF FUNCTION
    """ This function also takes as input the level selected by the user and 
    returns the list of answers corresponding to quiz selected. """
    
    if level == "easy":
        return answer_easy
    if level == "medium":
        return answer_medium
    if level == "hard":
        return answer_hard

quiz = quiz_select(level)
answer = answers_select(level)


def replace_quiz(quiz_string, list_answer_element, blank_space_element):
    # Comment --> USE OF FUNCTION
    """ This function takes as input a string and 2 lists and returns as output, a string. 
    This function modifies the text of the quiz when a correct answer is given by replacing the 
    corresponding blanks by the correct answer. """
    
    replaced = []
    quiz_string = quiz_string.split()
    for string in quiz_string:
        if blank_space_element in string:
            string = string[0:11].replace(str(blank_space_element), str(list_answer_element)) + string[11:]
            replaced.append(string)
        else:
            replaced.append(string)
    quiz_string = " ".join(replaced)
    return quiz_string


def print_result(flag):
    # Comment --> USE OF FUNCTION
    """ This function takes a "flag" variable as input and prints the end results as output. """
    
    if flag == 0:
        print ("Run the program again and try a different level  :-)")
    else:
        print ("AWESOME!!!! You win. Try playing again with another level\n")
        print ("You'll have to run the program again  :-)")


def play_game(quiz, list_answer, blank_spaces):
    # Comment --> USE OF FUNCTION
    """ This function takes a string and 2 lists as input and outputs the game in itself. User are prompted
        to enter answer and either are prompted again to give the next answer if the previous answer is correct or
        to try again if the user gives an incorrect answer. The game will return "BRAVO!" if all the answers are correct and
        "GAME OVER" if failed to provide all the correct answers. """
    
    g = 1  # Number of guesses
    n = 1  # Blank number
    flag = 1  # A "flag" variable
    while n <= len(blank_spaces) and g <= number_of_guess:
        user_input_n = raw_input("What should be substituted for _____" + str(n) + "_____" + ": ").upper()
        if correct_guess(user_input_n,answer[n-1]) != None:
            print "\nCORRECT! \n\nThe current paragraph reads as such -->"
            quiz = replace_quiz(quiz, answer[n-1], blank_spaces[n-1])
            if n == 8:
                break
            print quiz + "\n"
            n += 1      
        else:
            if g < number_of_guess:
                print ("This isn't the correct answer! Let's try again you have ") + str(number_of_guess - g) + (" tries left")
                g += 1
            else:
                print ("\n\nGAME OVER!")
                flag = 0
                break

    print_result(flag)


# Now, Let's play the game

# Prints the chosen "quiz" after showing all the possible choices of levels
print quiz_select(level)
play_game(quiz, answer, blank_spaces)
