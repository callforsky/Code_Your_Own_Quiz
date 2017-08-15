# I design this game to be a Space history refresher.
# The game has to have 3 levels and each level contains 4 or more blanks to fill

# Use a dictionary to store all the background data for the game
quiz = {
    'Easy': {
        'phrase': "In year __1__, __2__ program sent 3 astronauts to the moon. "
        "__3__ is the first person to walk on the moon. "
        "This unprecedented manned Moon landing mission beat Soviet Union that "
        "sent first human to journey into outer space in year __4__.",
        'answers': ['1969,', 'Apollo', 'Neil Armstrong', '1961.']
    },
    'Medium': {
        'phrase': "In year __1__, Soviets launched the first artificial "
        "satellite, __2__, into space. In year __3__, the first U.S. "
        "satellite, __4__, went into orbit.",
        'answers': ['1957,', 'Sputnik 1,', '1958,', 'Explorer 1,']
    },
    'Hard': {
        'phrase': "In year __1__, Chinese astronaut, __2__, became the first "
        "person sent into space by Chinese space program. In year __3__, "
        "Chinese astronaut, __4__, became the first Chinese citizen to carry "
        "out a spacewalk in the mission of Shenzhou 7.",
        'answers': ['2003,', 'Yang Liwei,', '2008,', 'Zhai Zhigang,']
    }
}

# a list of string of blanks
blanks = ['__1__', '__2__', '__3__', '__4__']

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

def check_if_blank(word, blanks):
    """
    This function checks if the word is a blank defined in the list blanks

    Inputs:
        word: any string. In this function it is expected to be one of the
            splitted word from the quesiton phrase
        blanks: the list of blanks

    Returns:
        returns True if word is a defined blank
    """
    for each in blanks:
        if each in word:
            return True

def print_answer(level, replaced, word, index):
    """
    This function prints the congratulation message at first. Then it replaces
    the blank with the answer and print the answer. At last, it increases the
    index by one so the loops will move to next blank

    Inputs:
        level: a value returned by choose_level(), the difficulty level.
            values are 'Easy', 'Medium', or 'Hard'
        replaced: a saved phrase where blanks are replaced with answers, start
            from the original question phrase
        word: in this function it is really one of the blanks
        index: the yet updated index, which will be updated in this function

    Returns:
        index: udpated index as the user fills the blank correctly
        replaced: update the replaced phrase to keep the answers filled in
                  earlier
    """
    print "You're correct!"
    replaced = replaced.replace(word, quiz[level]['answers'][index])
    #print replaced
    print replaced
    # move to next blank, update the index
    index += 1
    return index, replaced


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
    # Set the initial question phrase whose blanks will be replaced
    replaced = quiz[level]['phrase']
    # start checking each word in the question phrase
    for word in quiz[level]['phrase'].split():
        if check_if_blank(word, blanks):
            guesses = 0
            while guesses < guess_num:
                response = raw_input("Please fill in the " + index_map[index] +
                                     " blank: ")
                if response not in quiz[level]['answers'][index]:
                    guesses += 1
                    print "Sorry, wrong answer. Please try again."
                else:
                    index, replaced = print_answer(level, replaced, word, index)
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
