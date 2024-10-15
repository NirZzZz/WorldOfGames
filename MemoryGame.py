import random
from time import sleep


def generate_sequence(_difficulty):
    seq = []
    for i in range(_difficulty):
        num = random.randint(1, 101)
        seq.append(num)
    print(seq, end="")
    sleep(0.7)
    print("\r      ")
    return seq


def get_list_from_user(_difficulty):
    while True:
        try:
            user_input = input(f"Please write the {_difficulty} numbers: ")
            user_input = user_input.split()
            user_input = [int(num) for num in user_input]
            if 1 <= len(user_input) <= _difficulty:
                return user_input
            else:
                print(f"Please write down {_difficulty} numbers")
        except ValueError:
            print("Invalid input, try again")


def is_list_equal(a, b):
    return a == b


def play(difficulty):
    seq = generate_sequence(difficulty)
    user_input = get_list_from_user(difficulty)
    if is_list_equal(seq, user_input):
        print("You da best!")
        return True
    else:
        print("You lost, don't be arrogant try a lower difficulty level")
        return False
