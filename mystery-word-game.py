# =============================================================================
# I M P O R T S
# =============================================================================

import string


# =============================================================================
# F U N C T I O N S
# =============================================================================

def guess_match(computer_chosen_word, guess):
    """
    Function that takes the computer's chosen word and user's guess as
    arguments and returns a boolean indicating whether or not that guess
    occurs within the computer's chosen word. !!! Function assumes the
    guess has already been checked for validity outside the function !!!

    :param computer_chosen_word: string - the word chosen by the computer.
    :param guess: string - the letter guessed by the user.
    :return: bool - True if guess is in computer_chosen_word, false if not.
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

    :param entry: bool - the value returned by the function guess_match.
    :param prior_count: int - how many prior incorrect guesses have been made.
    :return current_count: int - updated count of incorrect guesses.
    """

    if entry is False:
        current_count = prior_count + 1

    return current_count


def fill_in_blank(computer_chosen_word, replicated_word, letter_guessed):
    """
    Function that takes the computer's chosen word, the current letter guessed
    (letter_guessed), and the current state of the user's correct guesses
    (replicated_word) and adds the guessed letter to replicated_word in all
    appropriate places.

    :param computer_chosen_word: string - the word chosen by the computer.
    :param replicated_word: string - current state of the user-guessed word.
    :param letter_guessed: string - the letter guessed by the user.
    :return replicated_word: string - updated state of the user-guessed word.
    """
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

    :param computer_chosen_word: string - the word chosen by the computer.
    :return: NONE
    """
    wrong_guesses = 0
    all_user_guesses = []
    replicated_word = "_" * len(computer_chosen_word)
    ACCEPTED_LETTERS = set(string.ascii_lowercase)

    while (wrong_guesses < 8) and ("_" in replicated_word):

        user_guess = input("Guess ONE letter: ")

        if len(user_guess) > 1:
            print("Your guess is too long. Enter ONE letter only.")
        elif user_guess.lower() not in ACCEPTED_LETTERS:
            print("Invalid character entered. Please enter only characters found within the English alphabet.")
        elif user_guess.lower() in all_user_guesses:
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


# NOTE TO SELF: Next step will be to track which letters HAVEN'T been guessed
#               and print them after each valid guess.
# NOTE TO SELF: Next step will be to reveal word to user if it wasn't guessed.
# NOTE TO SELF: Next step will be to implement a check after a game ends to see
#               whether or not the user would like to play another game. If so,
#               run game again. If not, exit.


# =============================================================================
# O T H E R  C O D E
# =============================================================================

# NOTE 1: Test word will be "aardvark"

chosen_word = "aardvark"

print()
print(f"The computer has chosen a word. It is {len(chosen_word)} letter(s) long.")

guess_prompt_loop(chosen_word)
