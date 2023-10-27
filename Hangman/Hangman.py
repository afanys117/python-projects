import random
import hangmanArt
import hangmanWordList

lifes = 6

print(hangmanArt.logo)

chosen_word = random.choice(hangmanWordList.word_list)
# print(chosen_word)

display = []

for num in range(0, len(chosen_word)):
    display.append("_")

chosenWordChar = list(chosen_word)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter\n").lower()

    if guess in display:
        print(f"You have already entered the letter {guess}.")
    else:
        for num in range(len(chosen_word)):
            if chosen_word[num] == guess:
                display[num] = guess

    print(display)

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.\nYou lose a life.")
        lifes -= 1

    if "_" not in display:
        end_of_game = True
        print("You won")
    elif lifes == 0:
        end_of_game = True
        print("You lost")

    print(hangmanArt.stages[lifes])
