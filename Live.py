from GuessGame import play as guess_game
from MemoryGame import play as memory_game
from CurrencyRoulette import play as currency_roulette
from MainScores import add_score, init_db


def welcome():
    name = input("please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.")
    return name


games = {
    1: {"name": "Memory Game", "game": memory_game},
    2: {"name": "Guess Game", "game": guess_game},
    3: {"name": "Currency Roulette", "game": currency_roulette}
}


def get_user_input(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Invalid number, must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print(f"Invalid input, please enter a number between {min_val} and {max_val}.")


def load_game(name):
    game_prompt = """
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
"""
    difficulty_prompt = """
Please choose game difficulty (1 to 5)
"""
    chosen_game = get_user_input(game_prompt, 1, 3)
    print(f"You chose to play {games[chosen_game].get('name')}, enjoy!")
    game_difficulty = get_user_input(difficulty_prompt, 1, 5)
    print(f"You chose difficulty {game_difficulty}.")
    game_play = games[chosen_game].get("game")
    win = game_play(game_difficulty)
    if not win:
        pass
    else:
        init_db()
        add_score(name, game_difficulty)
