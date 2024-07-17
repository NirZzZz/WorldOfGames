import random


def generate_number(_diffictlty):
    secret_number = random.randint(1, _diffictlty)
    return secret_number


def get_guess_from_user(_difficulty):
    while True:
        try:
            user_number = int(input(f"Please guess a number between 1 and {_difficulty}:"))
            if 1 <= user_number <= _difficulty:
                return user_number
            else:
                print(f"You didn't get it right, Please guess a number between 1 and {_difficulty}")
        except ValueError:
            print("Invalid input")


def compare_results(a, b):
    return a == b


def play(difficulty):
    guess = get_guess_from_user(difficulty)
    secret = generate_number(difficulty)
    if compare_results(guess, secret):
        print("You Won!")
        return True
    else:
        print("Haha loser!")
        return False
