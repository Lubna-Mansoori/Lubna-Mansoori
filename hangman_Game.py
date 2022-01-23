import random
import time

print("Welcome to Hangman Game")
name =input("Enter your name: ")
print("All the best "+name)
time.sleep(2)
print("Lets start the Game...")
time.sleep(3)

def main():
    global length
    global count
    global display
    global already_guessed
    global play_game
    global word
    global main_word
    words_to_guess = ["stone","line","books","picture","pen","case","rose","globe"]
    word = random.choice(words_to_guess)
    main_word = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = " "


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes , n = no ")
    while play_game not in ["Y","N","y","n"]:
        play_game = input("Invalid Input \n Do you want to play again? \n y = yes , n = no ")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing")
        exit()


def hangman():
    global count
    global display
    global already_guessed
    global word
    limit = 5
    global main_word
    global finder
    global counter
    finder = 0
    counter = 0
    guess = input("This is the Hangman word: "+ display+ " Enter your guess: \n")
    guess=guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, Try a letter \n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        #print(word)
        display = display[:index] + guess + display[index + 1:]
        print(display)

    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count = count + 1
        if count == 1:
           print("Wrong guess... " + str(limit-count) + " guesses remaining \n")
        if count == 2:
           print("Wrong guess... " + str(limit-count) + " guesses remaining \n")
        if count == 3:
           print("Wrong guess... " + str(limit-count) + " guesses remaining \n")
        if count == 4:
           print("Wrong guess... " + str(limit-count) + " guesses remaining \n")
        if count == 5:
            print("Wrong guess... You are HANGEDDD \n")
            print("The word was: " ,already_guessed,main_word)
            play_loop()

    if word == "_" * length:
        print("Congrats you have guessed the word Correctly. \n It is "+ display)
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()
