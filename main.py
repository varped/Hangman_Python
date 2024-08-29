"""
This program implements the game hangman where one player chooses a secret word
and the other player guesses letters.
"""

def secret_word_input1(secret_word: str) -> bool:
    """
    This function takes the user's input for the secret word and
    continues asking the user until the input is valid
    :param secret_word: str
    :return: bool
    """
    secret_word = secret_word
    for char in str(secret_word):
        if char == '?' or char == ' ':
            return True
    return False

def secret_word_input2():
    """
    This function will check if the secret word is valid to use for the game.
    :return: str
    """
    secret_word = str(input('Please enter a word to be guessed that does not contain ? or white space: ')).strip()
    while secret_word_input1(secret_word):
        secret_word = str(input('Please enter a word to be guessed that does not contain ? or white space: ')).strip()
    return secret_word

def hide_secret_word(secret_word: str) -> str:
    """
    This function takes the user's input for the secret word and
    converts each letter to a question mark for the player to guess.
    :param secret_word: str
    :param guessed_char: str
    :return: str
    """
    display_word = '?' * len(secret_word)
    return display_word

def hangman_pic(guess_count):
    """
    This function displays the hangman figure when the user guesses a character
    that is not in the word to be guessed.
    :param guess_count: int
    :return: str
    """
    if (guess_count == 0):
        pass
    elif (guess_count == 1):
        print("|")
    elif (guess_count == 2):
        print("|")
        print("0")
    elif (guess_count == 3):
        print("|")
        print("0")
        print("|")
    elif (guess_count == 4):
        print(" | ")
        print(" 0 ")
        print("/| ")
    elif (guess_count == 5):
        print(" | ")
        print(" 0 ")
        print("/|\\")
    elif (guess_count == 6):
        print(" | ")
        print(" 0 ")
        print("/|\\")
        print("/  ")
    elif (guess_count >= 7):
        print(" | ")
        print(" 0 ")
        print("/|\\")
        print("/ \\")

def check_if_guess_valid(guessed_chars) -> str:
    """
    This function checks if the guess is valid as it should only be a single character.
    :param guessed_chars: str
    :return: str
    """
    while True:
        guess = input(f'Please enter your next guess: ').strip().lower()
        if len(guess) != 1:
            print(f'You can only guess a single character.')
        elif guess == ' ':
            print(f'You must enter a character.')
        elif guess in guessed_chars:
            print(f'You already guessed the character: {guess}')
        else:
            return guess

def is_guess_in_word(secret_word: str, display_word: str, guessed_chars: str, guess_count: int):
    """
    This function checks if the guessed character is in the secret word.
    If so, it will replace the character in the hidden word and output a list
    of the characters that the user guessed so far.
    :param secret_word: str
    :param display_word: str
    :param guessed_chars: str
    :param guess_count: int
    :return: display_word, guessed_chars, guess_count
    """
    guess = check_if_guess_valid(guessed_chars)
    guessed_chars.append(guess)
    if guess in secret_word:
        display_word_list = list(display_word)
        for i, char in enumerate(secret_word):
            if char == guess:
                display_word_list[i] = guess
        display_word = ''.join(display_word_list)
    else:
        guess_count += 1
    return display_word, guessed_chars, guess_count

def ask_for_guess() -> None:
    """
    This function will interpret the user's guess to play hangman.
    """
    guessed_chars = []
    guess_count = 0
    secret_word = secret_word_input2()
    display_word = hide_secret_word(secret_word)

    while guess_count < 7:
        hangman_pic(guess_count)
        print(display_word)
        print(f'So far you have guessed: {", ".join(sorted(guessed_chars))}')
        display_word, guessed_chars, guess_count = is_guess_in_word(secret_word, display_word, guessed_chars, guess_count)
        if guess_count == 7:
            hangman_pic(guess_count)
            print(f'You failed to guess the secret word: {secret_word}')
        elif secret_word == display_word:
            print(f'You correctly guessed the secret word: {secret_word}')
            break
def main():
    ask_for_guess()

if __name__ == "__main__":
        main()