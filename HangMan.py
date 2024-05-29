import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
from hangman_art import win
from hangman_art import loose
choosen_word = random.choice(word_list)
lives = 6
guessed_word = []
for n in range(0 , len(choosen_word)):
    guessed_word += '_'
print(logo)
print(choosen_word)
while '_' in guessed_word and lives > 0:
    guess = input("Type a letter: c").lower()
    if guess in choosen_word:
        for n in range(0 , len(choosen_word)):
            if choosen_word[n] == guess:
                guessed_word[n] = guess
        print(stages[lives])
        print(*guessed_word)
    else:
        lives -= 1
        print(stages[lives])
        print(*guessed_word)

if '_' in guessed_word:
    print(loose)
else:
    print(win)