from random import randint
print('Welcome to the number guessing game!\n I am thinking of a number between 1 and 100.\n')
difficulty_level = input('Choose a difficulty. Type "easy" or "hard": ').lower()
number = randint(1, 100)
def check_guess(number: int, guess: int):
     if guess < number:
        print('Too low\n Guess again')
        return False
     elif guess > number:
        print('Too high\n Guess again')
        return False
     elif guess == number:
        print('You win!!!')
        return True
     else:
         print('you lose')
def set_difficulty(): 
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5
    elif difficulty_level != 'easy' and difficulty_level != 'hard':
            print('please choose hard or easy difficulty')
            exit()
attempts_left = set_difficulty()
while attempts_left > 0:
    print(f'you have {attempts_left} attempts remaining to guess the number.')
    guess = int(input('Make a guess. '))
    attempts_left -= 1
    guess_is_right = check_guess(number, guess)
    if guess_is_right:
         break
    