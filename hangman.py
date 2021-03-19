import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lettersWord = list(secretWord)
    for letter in lettersWord[:]:
        if letter in lettersGuessed:
            lettersWord.remove(letter)
    if len(lettersWord) == 0:
        return True
    else:
        return False
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += "_ "
    return guessedWord

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    lettersList = list(letters)
    for letter in lettersGuessed:
        if letter in letters:
            lettersList.remove(letter)
    return ''.join(lettersList)
            
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is" ,len(secretWord), "letters long.")
    guessesLeft = 8
    lettersGuessed = []
    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("You have" ,guessesLeft, "guesses left.")
        print("Available letters:" ,getAvailableLetters(lettersGuessed))
        user_input = input("Please guess a letter: ")
        if user_input not in lettersGuessed:
            lettersGuessed.append(user_input)
            if user_input in secretWord:
                print("Good guess:" ,getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("-------------")
                    print("Congratulations, you won!")
                    break
            else:
                print("Oops! That letter is not in my word:" ,getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
                if guessesLeft == 0:
                    print("-------------")
                    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
                    break
        else:
            print("Oops! You've already guessed that letter:" ,getGuessedWord(secretWord, lettersGuessed))

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)