from data import data
from random import choice


print('Hello gamer, test your knowledge of how popular celebrities are')
def game_started():
    first_celeb = choice(data)
    second_celeb = choice(data)
    while first_celeb == second_celeb:  # Ensure the two celebrities are different
        second_celeb = choice(data)
    return first_celeb, second_celeb
def next_round(celeb):
    new_celeb = choice(data)
    while celeb == new_celeb:
        new_celeb = choice(data)
    return new_celeb

def find_higher(chosen_celeb, one, two, score=1):
    game_continue = True
    if chosen_celeb == "1":
        current_celeb = one
        if current_celeb['follower_count'] > two['follower_count']:
            print(f'you win, next round we go\n current score is {score}')
        else:
            print('u lose')
            game_continue = False
    else:
        current_celeb = two
        if current_celeb['follower_count'] > one['follower_count']:
            score += 1
            print(f'you win, next round we go\n current score is {score}')
        else:
            print('u lose')
            game_continue = False
    return current_celeb, game_continue


still_playing = True
score = 0
current_celeb = {}
while still_playing:
    if score == 0:
        celeb_a, celeb_b = game_started()
        print(f'Guess the celeb with the higher following count\n option one is {celeb_a["name"]} from {celeb_a["country"]} or option two is {celeb_b["name"]} from {celeb_b["country"]}')
        chosen_celeb = input(f"Select 1 for: {celeb_a['name']} or 2 for: {celeb_b['name']}: ")
        answer = find_higher(chosen_celeb, celeb_a, celeb_b)
        current_celeb, still_playing = answer

    else:
        new_celeb = next_round(current_celeb)
        print(f"which one is higher, option one is {current_celeb['name']} or option two is {new_celeb['name']}")
        chosen_celeb = input(f"Select 1 for: {current_celeb['name']} or 2 for: {new_celeb['name']}: ")
        answer = find_higher(chosen_celeb, current_celeb, new_celeb, score)
        still_playing = False if answer(1) == False else True
    if still_playing == False:
        score = 0