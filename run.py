import random

# words imported from the website https://www.hangmanwords.com/words
WORDS = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie'
]

# hagman art from the website https://inventwithpython.com/bigbookpython/project34.html

HANGMAN = {
    6:
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    5:
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    4:
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    3:
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    2:
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    1:
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    0:
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''}

def print_hangman_word(word, letters=[]):
    '''
    Prints a word letter by letter. If a letter in the word is
    not yet guessed, it prints an underscore character
    '''

    for letter in word:
        if letter in letters:
            print(letter, end='')
        else:
            print('_', end='')
    print()

word = random.choice(WORDS)
print(word)
print_hangman_word(word)

lives = 7
letters_in_word = {letter for letter in word}
print(letters_in_word)
correct_letters = []
wrong_letters = []
print_hangman_word(word, correct_letters)

while lives > 0 and len(correct_letters) != len(letters_in_word):
    # verification of the user's input
    while True:
        guess_letter = input('guess a letter: ').lower().strip()
        if not guess_letter.isalpha():
            print('Invalid input! Only the letters are permitted!')
        elif len(guess_letter) != 1:
            print('Invalid input! The guess should be only one letter!')
        else:
            break
    # verification of the correct guess
    if guess_letter in correct_letters or guess_letter in wrong_letters:
        print("you've already guessed this letter")
    elif guess_letter not in letters_in_word:
        lives -= 1
        print(f'the letter {guess_letter} is not in the word! Lives: {lives}')
        print(HANGMAN[lives])
        wrong_letters.append(guess_letter)
        if lives == 0:
            break
    else:
        print(f'good one! the letter {guess_letter} is in the word!')
        correct_letters.append(guess_letter)
    print_hangman_word(word, correct_letters)

if lives == 0:
    print("you've lost")
else:
    print("you win!!!")