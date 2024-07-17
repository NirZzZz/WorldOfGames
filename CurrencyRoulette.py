import random
import requests


def get_money_interval(generated_number, _difficulty):
    url = ('https://cdn.jsdelivr.net/npm/@fawazahmed0/'
           'currency-api@latest/v1/currencies/usd.json')
    response = requests.get(url)
    conversion_rate = float(response.json().get('usd').get('ils'))
    total = (generated_number * conversion_rate)
    upper_bound = (total + (5 - _difficulty))
    lower_bound = (total - (5 - _difficulty))
    return upper_bound, lower_bound


def get_guess_from_user():
    generated_number = random.randint(1, 101)
    print(f"{generated_number} USD")
    while True:
        try:
            guess = float(input("guess how much is it in ILS: "))
            if 1 <= guess <= 500:
                return guess, generated_number
            else:
                print("It doesn't make sense, the conversion rate "
                      "was never higher then 5 or below 1, "
                      "You got another chance")
        except ValueError:
            print("Invalid input, try again")


def play(difficulty):
    guess, generated_number = get_guess_from_user()
    upper_bound, lower_bound = get_money_interval(generated_number, difficulty)
    if upper_bound >= guess >= lower_bound:
        print("Great, you won!")
        return True
    else:
        print("Loser!")
        return False
