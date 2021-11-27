# =============================================================================
# F U N C T I O N S
# =============================================================================

def guess_match(computer_choice, guess):
    """
    Function that takes the computer's chosen word and user's guess as
    arguments and returns a bool indicating whether or not that guess occurs
    within the computer's chosen word. !!! Function assumes the guess has
    already been checked for validity outside the function !!!
    """

    for letter in computer_choice:
        if guess.lower() == letter:
            return True

    return False


# =============================================================================
# O T H E R  C O D E
# =============================================================================
# NOTE 1: Test word will be "try"
# NOTE 2: Consider making a separate doc defining a constant for all English
#         letters (upper AND lower? Likely unnecessary) that can be used to
#         check against.

chosen_word = "try"
user_guess = input("The computer has chosen a word. Guess ONE of the letters \
in that word: ")

print(f"Your guess is {guess_match(chosen_word, user_guess)}.")
