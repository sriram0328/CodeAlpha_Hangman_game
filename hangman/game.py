import random
import stages

word_list = ['codealpha','code','alpha','python','internship',
             'apple','banana','cat','dog','elephant','beautiful',
             'ugly','love','hate','hello','namaste','guitar','piano','icecream','keyboard']

selected_word = random.choice(word_list)
lives = 6

print(selected_word)
show = []

for i in range(len(selected_word)):
    show += '_'
print(show)

gameOver = False

while not gameOver:
    guess_letter = input("Guess a letter:")
    for place in range(len(selected_word)):
        letter = selected_word[place]
        if letter == guess_letter:
            show[place] = guess_letter
    print(show)
    if guess_letter not in selected_word:
        lives -= 1
        if lives == 0:
            gameOver = True
            print()
            print()
            print("You lost the game!!")
    if '_' not in show:
        gameOver = True
        print("YOU WIN THE GAME YAYYYYYY!!!!")
    print(stages.stage[lives])

