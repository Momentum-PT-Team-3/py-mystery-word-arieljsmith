# =============================================================================
# I M P O R T S
# =============================================================================

import string
import random


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


def split_by_difficulty(word_list):
    """
    Function that takes a list of words and sorts that list into three
    groups (easy, normal, or hard) depending on the length of each word.

    :param word_list: list - list of words computer can choose from
    :return easy_words: list - list of words between 1-5 characters
    :return normal_words: list - list of words between 6-8 characters
    :return hard_words: list - list of words of 9 or more characters
    """
    easy_words, normal_words, hard_words = [], [], []

    for word in word_list:
        if len(word) <= 5:
            easy_words.append(word)
        elif 5 < len(word) <= 8:
            normal_words.append(word)
        else:
            hard_words.append(word)

    return easy_words, normal_words, hard_words


def select_difficulty(easy_list, normal_list, hard_list):
    """
    Function that takes three lists of words separated according to word
    length, asks the user for the desired game difficulty level, and returns
    the list associated with that difficulty level.

    :param easy_list: list - list of words between 1-5 characters
    :param normal_list: list - list of words between 6-8 characters
    :param hard_list: list - list of words of 9 or more characters
    :return easy_list, normal_list, OR hard_list: list - see parameters
    """
    valid_input = False

    while not valid_input:
        desired_difficulty = input("Select game difficulty (easy, normal, hard): ")
        if desired_difficulty.lower() == "easy" or desired_difficulty.lower() == "normal" or desired_difficulty.lower() == "hard":
            valid_input = True
            if desired_difficulty.lower() == "easy":
                return easy_list
            elif desired_difficulty.lower() == "normal":
                return normal_list
            else:
                return hard_list
        else:
            print("Invalid input. Please only enter 'easy', 'normal', or 'hard'.")
            print()


def request_continuation_input():
    """
    Function that, when called, prompts the user on their desire to play one more round.
    Returns the user's answer as True or False.

    :return new_continuation_state: boolean - indicate's user's desire to play another round
    """

    continue_loop_check = False

    while continue_loop_check is False:

        intent_to_continue = input("Would you like to play again? [y/n]: ")

        if intent_to_continue.lower() == "y":
            new_continuation_state = True
            continue_loop_check = True
            print("Sweet! Let's go.")
        elif intent_to_continue.lower() == "n":
            new_continuation_state = False
            continue_loop_check = True
            print("Thank you for playing!")
        else:
            print('Invalid input. Please only enter "y" or "n".')

        print()

    return new_continuation_state


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
    unguessed_letters = sorted(list(ACCEPTED_LETTERS))

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
            unguessed_letters.remove(user_guess.lower())
        else:
            print("Your guess is correct!")
            all_user_guesses.append(user_guess.lower())
            replicated_word = fill_in_blank(computer_chosen_word, replicated_word, user_guess)
            unguessed_letters.remove(user_guess.lower())

        print(f"WORD SO FAR: {replicated_word}")
        print(f"UNUSED LETTERS: {unguessed_letters}")
        print()

    if "_" not in replicated_word:
        print("Congratulations, you guessed the word!")
    else:
        print(f'So close! The word was "{computer_chosen_word}".')

    return    


def game_loop():
    """
    """
    continuation = True

    while continuation is True:
        continuation = False
        selected_difficulty_word_list = select_difficulty(easy_list, normal_list, hard_list)
        print()

        computer_chosen_word = random.choice(selected_difficulty_word_list)

        print()
        print(f"The computer has chosen a word. It is {len(computer_chosen_word)} letter(s) long.")

        guess_prompt_loop(computer_chosen_word)

        continuation = request_continuation_input()

    return


# =============================================================================
# O T H E R  C O D E
# =============================================================================

with open("words.txt", "r") as big_forkin_word_file:
    big_forkin_word_list = big_forkin_word_file.readlines()
    new_big_forkin_word_list = []
    for word_entry in big_forkin_word_list:
        new_big_forkin_word_list.append(word_entry[:-1])

    easy_list, normal_list, hard_list = split_by_difficulty(new_big_forkin_word_list)

    game_loop()

# CONSIDER SETTING UP DIFFICULTY INTO DICTIONARIES

# =============================================================================
# M I S C E L L A N Y
# =============================================================================

# NOTE: Might use this guy if I have time to toss him in. Time will tell.

#                             ▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓▓
#                           ▓▓░░░░░░▓▓    ▓▓░░░░░░░▓▓
#                          ▓▓░░░██░░░░▓▓▓▓░░░░██░░░░▓▓
#     ▒▒▒▒▒▒▒▒▒▒▒        ▒▒▒░░░░██░░░░░░░░░░░░██░░░░░▓▓
#   ▓▓░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#   ▓▓▓▓░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#   ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░▓▓
#     ▒▒▒▒▒▓░░░░▓░░░▓░░░▓░░░▓░░░▓░░░▓░░░▓░░░▓▒░░░░░░░░▓▓
#       ▓▓░▓▓░░▓▓░░▓▓░░▓▓░░▓▓░░▓▓░░▓▓░░▓▓░░▓░▒▒░░░░░░░▓▓
#         ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#                      ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#                    ▓▓▓▓▓░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░▓▓
#                   ▓▓░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░▒▓▓
#                  ▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░░▓▓░░▒▒░▓▓       ▒
#                    ▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░▓▓       ▒▒
#                     ▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓      ▒▒▒▒
#                        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓   ▓▓░░░▓
#                       ▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓░░░░░░░░▓▓▓░░░░░▓▓
#                       ▓▓░░░░▓▓          ▓▓░░░░▓▓▓▓▓▓░░░░░░░░░░▓▓
#                       ▓▓░░░░▓▓          ▓▓░░░░▓▓      ▒▒▒▒▒▓▓▓
#                       ▓▓░░░░▓▓          ▓▓░░░░▓▓
#                        ▓▓▓▓▓▓            ▓▓▓▓▓▓
