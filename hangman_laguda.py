import random

def choose_word():
    words = ["python", "programming", "computer", "science", "coding", "designing", "development"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(incorrect_attempts):
    hangman_art = [
        '''
         ------
         |    |
         |
         |
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        '''
    ]

    return hangman_art[incorrect_attempts]

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = len(display_hangman(0))

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_attempts += 1
            print(f"Incorrect! You have {max_attempts - incorrect_attempts} attempts left.")
        else:
            print("Correct!")

        print(display_hangman(incorrect_attempts))
        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)

        if "_" not in word_display:
            print("Congratulations! You guessed the word.")
            break

    if "_" in word_display:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
