# The game has to have 3 levels and each level contains 4 or more blanks to fill
# I design this game to be a Space history refresher.

# Level 1: basic format of SQL.
lvl1 = [ "Easy", "In year ____, ____ program sent 3 astronauts to the moon. ____ is the first person to walk on the moon. This unprecedented manned Moon landing mission beat Soviet Union that sent first human to journey into outer space in year ____."]

lvl1_Ans = ['1969', 'Apollo', 'Neil Armstrong', '1961']

# Level 2: concat and wildcard search function
lvl2 = ["Medium", "In year ____, Soviets launched the first artificial satellite, ____, into space. In year ____, the first U.S. satellite, ____, went into orbit."]

lvl2_Ans = ['1957', 'Sputnik 1', '1958', 'Explorer 1']

# Level 3: insert and delete values from a table
lvl3 = ["Hard", "In year ____, Chinese astronaut, ____, became the first person sent into space by Chinese space program. In year ____, Chinese astronaut, ____, became the first Chinese citizen to carry out a spacewalk in the mission of Shenzhou 7."]

lvl3_Ans = ['2003', 'Yang Liwei', '2008', 'Zhai Zhigang']

# Open game, prompted to select the level, then run the relevant level based on the choice
def PlayGame():
    ''' Ask the player to select a difficulty level, then run the corresponding game  '''
    #defensive programming, prompt the user to enter the valid value
    while True:
        try:
            choice = int(raw_input("Welcome! I am going to test your knowledge of the history of Space Exploration! This game has 3 levels: 1-easy; 2-medium; 3-hard. Please enter the number to choose your challenge --> "))
        except ValueError:
            print "You must enter 1, 2, or 3 only!"
            continue

        if choice not in range(1,4):
            print "You must enter 1, 2, or 3 only!"
            continue
        else:
            # choice was successfully parsed, ready to exit the loop
            break
    # run the game based on player's difficulty choice
    if choice == 1:
        return QuestionAndAnswer(lvl1, lvl1_Ans)
    elif choice == 2:
        return QuestionAndAnswer(lvl2, lvl2_Ans)
    else:
        return QuestionAndAnswer(lvl3, lvl3_Ans)

def QuestionAndAnswer(question, answer):
    ''' Display the question at first. Ask the player to fill in the blank one by one. The game will not move to next blank until the user enter the correct answer '''
    print question[1]
    # will use the item_map below to translate item code to English language. we use it to tell player which blank they are on
    item_map = {1: 'first', 2:'second', 3:'third', 4:'fourth'}
    item = 1
    for word in question[1].split():
        if "____" in word:
            # loop on the same blank until the player enter the correct answer, I give the player 3 guesses, if not correct after 3 guesses, prompt the answer
            guesses = 0
            while guesses < 3:
                response = raw_input("Please fill in the " + item_map[item] + " blank: ")
                guesses += 1
                if response != answer[item-1]:
                    print "Sorry, wrong answer. Please try again."
                else:
                    print "You're correct! The " + item_map[item] + " blank should be " + answer[item-1]
                    # move to next blank, update the item order
                    item += 1
                    break

    return "Congratulation! You passed Level " + question[0] + " of this game!"

print PlayGame()
