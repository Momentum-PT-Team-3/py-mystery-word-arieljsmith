# Mystery Word

## Description

Implement the game of Mystery Word.

## Objectives

After completing this assignment, you should be able to:

- Create an interactive program.
- Read from a file.
- Choose a random value.
- Keep track of state.

## Details

## Normal Mode

You will implement the game Mystery Word. In your game, you will be playing
against the computer.

The computer must select a word at random from the list of words in the file
`words.txt` from this repository.

The game must be interactive; the flow of the game should go as follows:

1. Let the user choose a level of difficulty at the beginning of the program.
   Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
   characters; hard mode only has words of 8+ characters.

2. At the start of the game, let the user know how many letters the computer's
   word contains.

3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
   upper or lower case and it should not matter. If a user enters more than one
   letter, tell them the input is invalid and let them try again.

4. Let the user know if their guess appears in the computer's word.

5. Display the partially guessed word, as well as letters that have not been
   guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
   and d, the screen should display:

```
B _ _ B A _ D
```

A user is allowed 8 guesses. Remind the user of how many guesses they have left
after each round.

_A user loses a guess only when they guess incorrectly._ If they guess a letter
that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead,
print a message letting them know they've already guessed that letter and ask
them to try again.

The game should end when the user constructs the full word or runs out of
guesses. If the player runs out of guesses, reveal the word to the user when
the game ends.

When a game ends, ask the user if they want to play again. The game begins
again if they reply positively.

## Suggested Approach

- Pick one simple word to start with (don't worry about the word list at first), so that the user is guessing the same word each time.
- Write a function that accepts the user's guess and determines whether it is in the word or not.
- Figure out how you are going to keep track of right and wrong guesses.
- Write a function that repeats the above guessing process.
- Determine how the game ends.
- Once you've got the game working, move on to selecting a word at random. This [resource](https://realpython.com/read-write-files-python/#reading-and-writing-opened-files) will help with reading files.
- Generate a list of words from the `words.txt` file.
- Write a function that splits that list into multiple lists according to level.
- Write a function that obtains the level choice from the user.
- Write a function that selects a word at random from the appropriate list.
- Complete your program so that the user can choose a level and guess letters until they win or run out of guesses. 

## Hard Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "demon_words.py".

## Credit

This lab is based off a similar exercise in MIT's 6.00.1x course.
