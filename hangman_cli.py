chosen_word = 'hotty'
display = ['_'] * len(chosen_word)
ticker = 0
guess = ''
lives = 3
def have_guess():
    global guess
    guess = input('what is your guess?\n').lower()
def check_guess():
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        global lives
        lives -= 1
        if lives == 0:
            print('u lose')
while '_' in display:
     have_guess()
     check_guess()
     print(display)
     if lives == 0:
         break
if '_' not in display:
    print(f'you win the word is {display}')


