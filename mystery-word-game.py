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
    else:
        current_count = prior_count

    return current_count


def dict_transform(computer_chosen_word):
    """
    Takes the word chosen by the computer and makes it into a dictionary.
    """
    computer_word_dict = {}

    for letter in computer_chosen_word:
        computer_word_dict[letter.lower()] = 1

    for letter in computer_chosen_word:
        computer_word_dict[letter.lower()] += 1

    return computer_word_dict


def add_to_dict(user_guess_dict, guessed_letter, computer_word_dict):
    """
    Function that takes a guessed letter, and if it matches a key in
    the given computer_word_dict, adds that letter to the given
    user_guess_dict in the same quantity.
    """
    guessed_letter = guessed_letter.lower()

    if guessed_letter in computer_word_dict:
        if guessed_letter not in user_guess_dict:
            user_guess_dict[guessed_letter] = computer_word_dict[guessed_letter]
    pass


def guess_prompt_loop(computer_chosen_word):
    """
    Function that takes the computer's chosen word and repeats the guessing
    process until the computer's chosen word is guessed or the number of
    incorrect guesses hits 8.
    """
    wrong_guesses = 0
    entered_letters = 0
    computer_word_dict = dict_transform(computer_chosen_word)

    while (wrong_guesses < 8) and (entered_letters < len(computer_chosen_word)):

        user_guess = input("Guess ONE letter: ")
        wrong_guesses = incorrect_guess_tracker(guess_match(computer_chosen_word, user_guess), wrong_guesses)

        if guess_match(computer_chosen_word, user_guess) is False:
            print("Your guess is incorrect.")
        else:
            print("Your guess is correct!")
            entered_letters += 1

    return


# =============================================================================
# O T H E R  C O D E
# =============================================================================

# NOTE 1: Test word will be "try"
# NOTE 2: Consider making a separate doc defining a constant for all English
#         letters (upper AND lower? Likely unnecessary) that can be used to
#         check against.

chosen_word = "try"

print("The computer has chosen a word.")

guess_prompt_loop(chosen_word)
# wrong_guesses = 0
# user_guess = input("The computer has chosen a word. Guess ONE of the letters \
# in that word: ")

# print(f"Your guess is {guess_match(chosen_word, user_guess)}.")

# wrong_guesses = incorrect_guess_tracker(guess_match(chosen_word, user_guess), wrong_guesses)
# print(f"You have {wrong_guesses} incorrect guesses so far.")
