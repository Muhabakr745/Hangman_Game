import random

word_list = [
    "Computer",
    "Banana",
    "Elephant",
    "Sunshine",
    "Butterfly",
    "Strawberry",
    "Guitar",
    "Rainbow",
    "Watermelon",
    "Football",
    "Pancake",
    "Pencil",
    "Kangaroo",
    "Chocolate",
    "Telephone",
    "Sandwich",
    "Cucumber",
    "Birthday",
    "Crocodile",
    "Pizza"
]


# Function to get a word from the list
def get_word(lst):
    word = random.choice(lst).upper()
    return word


# Function to display the current hangman state
def display_hangman(tries):
    stages = [  # Final state: head, torso, both arms, both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # Head, torso, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # Head, torso, both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # Head, torso, one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # Head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # Head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # Initial state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


# Function to play the game
def play(word):
    word_completion = '_' * len(word)  # A string containing underscores for each letter in the chosen word
    guessed = False  # Signal flag
    guessed_letters = []  # List of already guessed letters
    guessed_words = []  # List of already guessed words
    tries = 6  # Number of tries
    print('Let\'s see if you are good for something other than watching TikTok!')
    print(display_hangman(6))
    print(word_completion)
    while not guessed and tries > 0:
        guess = input('Enter a letter or a whole word if you think you can').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Come on, focus, the letter is already there')
            elif guess not in word:
                print('Ha-Ha, loser')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Wow, I underestimated you')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Try reading more books, your memory level is quite disturbing')
            elif guess != word:
                print('Another useless try. TikTok generation...')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Enter a letter or a whole word if you think you can ')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('You did it! Congratulations!')
    else:
        print('Well, that was inevitable')


# Main function
def main():
    name = input('What is your name, loser? - ')
    play_again = 'y'

    while play_again.lower() == 'y':
        word = get_word(word_list)
        play(word)
        play_again = input('Do you want to play again? (y/n): ')

    print(f'Get lost, {name}!')


if __name__ == "__main__":
    main()
