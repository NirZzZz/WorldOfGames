from Live import welcome, load_game
from MainScores import run_flask_app

load_game(name=welcome())
run_flask_app()
