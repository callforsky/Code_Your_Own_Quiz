# I design this game to be a Space history refresher.
# The game has to have 3 levels and each level contains 4 or more blanks to fill

# Use a dictionary to store all the background data for the game
quiz = {
    'Easy': {
        'phrase': "In year ____, ____ program sent 3 astronauts to the moon. "
        "____ is the first person to walk on the moon. "
        "This unprecedented manned Moon landing mission beat Soviet Union that "
        "sent first human to journey into outer space in year ____.",
        'answers': ['1969', 'Apollo', 'Neil Armstrong', '1961']
    },
    'Medium': {
        'phrase': "In year ____, Soviets launched the first artificial "
        "satellite, ____, into space. In year ____, the first U.S. "
        "satellite, ____, went into orbit.",
        'answers': ['1957', 'Sputnik 1', '1958', 'Explorer 1']
    },
    'Hard': {
        'phrase': "In year ____, Chinese astronaut, ____, became the first "
        "person sent into space by Chinese space program. In year ____, "
        "Chinese astronaut, ____, became the first Chinese citizen to carry "
        "out a spacewalk in the mission of Shenzhou 7.",
        'answers': ['2003', 'Yang Liwei', '2008', 'Zhai Zhigang']
    }
}

# map index to English language, so users know which blank she is working on
index_map = {0: 'first', 1:'second', 2:'third', 3:'fourth'}

# Ask the player to select the difficulty level
def choose_level():
    """
    Prompt the user to input 'easy', 'medium', or 'hard' to select the
    difficulty level.

    Raises:
        If the user enters a non-string or invalid string, prompt the user to
        re-enter her selection.

        If the user enters an string other than 'easy', 'medium', or 'hard',
        prompt the user to re-enter.

    Returns:
        level: 'Easy', 'Medium', or 'Hard'
    """
    while True:
        try:
            level = str(raw_input("Welcome! I am going to test your knowledge "
            "of the history of Space Exploration! This game has 3 levels: "
            "easy; medium; hard. Please type the level that you want to "
            "challenge --> "))
        except ValueError:
            print "You must enter 'easy','medium', or 'hard'!"
            continue

        if level.lower() not in ['easy', 'medium', 'hard']:
            print "You must enter 'easy','medium', or 'hard'!"
            continue
        else:
            break
    return level.title()

def max_guess_allowed():
    """
    Prompt the user to input a number of guesses that she can make before
    she loses the game.

    Raises:
        The input number must be a positive integer greater than 0. Otherwise,
        prompt the user to re-enter

    Returns:
        guess_num: a positive integer greater than 0
    """
    while True:
        try: guess_num = int(raw_input("Please enter the number of guesses "
        "you can make before you lose --> "))
        except ValueError:
            print "You must enter a positive integer!"
            continue
        if not guess_num > 0:
            print "You must enter a positive integer!"
        else:
            break
    return guess_num

def win_game(level, guess_num):
    """
    Print the question and ask the user to user input the answer. The user
    has at most X guesses (defined by users). If the user inputs the correct
    answer, move to next blank. If the user inputs the wrong answer, ask the
    user to input again. If the max number of guesses is reached, restart the
    game completely. If the user fills all blanks correctly, print the
    congratulation phrase that reminds what difficulty level and end the game.

    Inputs:
        level: a value returned by choose_level(), the difficulty level.
               values are 'Easy', 'Medium', or 'Hard'
        guess_num: a value returned by max_guess_allowed(). A positive integer

    Returns:
        This function returns False if the user did not answer all blanks within
        the max number of guesses they set earlier
    """
    # print the question at first
    print quiz[level]['phrase']
    # Set the index, start from first blank
    index = 0
    for word in quiz[level]['phrase'].split():
        if "____" in word:
            guesses = 0
            while guesses < guess_num:
                response = raw_input("Please fill in the " + index_map[index] +
                                     " blank: ")
                if response != quiz[level]['answers'][index]:
                    guesses += 1
                    print "Sorry, wrong answer. Please try again."
                else:
                    print "You're correct!"
                    # move to next blank, update the item order and reset guesses
                    index += 1
                    # reset the guess number
                    guesses = 0
                    break
            # return False to trigger the recursive function in main()
            if guesses == guess_num:
                print "You guessed "+str(guess_num)+" wrong. Restart game now."
                return False

def main():
    """
    This is the main function that consolidates all modules and execute the game
    """
    level = choose_level()
    guess_num = max_guess_allowed()
    if win_game(level, guess_num) != False:
        print "Congratulation! You passed Level " + level + " of this game!"
    else:
        main()

# run the game by calling the main control
main()
