# =============================================================================
# F U N C T I O N S
# =============================================================================

def guess_match(computer_chosen_word, guess):
    """
    Function that takes the computer's chosen word and user's guess as
    arguments and returns a boolean indicating whether or not that guess
    occurs within the computer's chosen word. !!! Function assumes the
    guess has already been checked for validity outside the function !!!
    """
    guess = guess.lower()

    for letter in computer_chosen_word:
        if guess == letter.lower():
            return True

    return False


def incorrect_guess_tracker(entry, prior_count):
    """
    Function that takes an entry (from the guess_match function) and the
    count up until the point this function is called and adds to the running
    total if the entry is false.
    """

    if entry is False:
        current_count = prior_count + 1

    return current_count


def fill_in_blank(computer_chosen_word, replicated_word, letter_guessed):
    current_index = 0
    replicated_word_list = list(replicated_word)

    for character in computer_chosen_word:
        if character.lower() == letter_guessed.lower():
            replicated_word_list[current_index] = letter_guessed.lower()
        current_index += 1

    replicated_word = "".join(replicated_word_list)

    return replicated_word


def guess_prompt_loop(computer_chosen_word):
    """
    Function that takes the computer's chosen word and repeats the guessing
    process until the computer's chosen word is guessed or the number of
    incorrect guesses hits 8.
    """
    wrong_guesses = 0
    all_user_guesses = []
    replicated_word = "_" * len(computer_chosen_word)

    while (wrong_guesses < 8) and ("_" in replicated_word):

        user_guess = input("Guess ONE letter: ")

        if user_guess.lower() in all_user_guesses:
            print("You already guessed that letter. Try again.")
        elif guess_match(computer_chosen_word, user_guess) is False:
            print("Your guess is incorrect.")
            all_user_guesses.append(user_guess.lower())
            wrong_guesses = incorrect_guess_tracker(guess_match(computer_chosen_word, user_guess), wrong_guesses)
        else:
            print("Your guess is correct!")
            all_user_guesses.append(user_guess.lower())
            replicated_word = fill_in_blank(computer_chosen_word, replicated_word, user_guess)

        print(replicated_word)
        print()

    return


# =============================================================================
# O T H E R  C O D E
# =============================================================================

# NOTE 1: Test word will be "try"
# NOTE 2: Consider making a separate doc defining a constant for all English
#         letters (upper AND lower? Likely unnecessary) that can be used to
#         check against.

chosen_word = "aardvark"

print()
print("The computer has chosen a word.")

guess_prompt_loop(chosen_word)
# wrong_guesses = 0
# user_guess = input("The computer has chosen a word. Guess ONE of the letters \
# in that word: ")

# print(f"Your guess is {guess_match(chosen_word, user_guess)}.")

# wrong_guesses = incorrect_guess_tracker(guess_match(chosen_word, user_guess), wrong_guesses)
# print(f"You have {wrong_guesses} incorrect guesses so far.")
