from flask import Flask
import sqlite3
import os

app = Flask(__name__)


def init_db():
    if not os.path.exists('scores.db'):
        conn = sqlite3.connect('scores.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                username TEXT PRIMARY KEY,
                score INTEGER
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized.")
    else:
        print("Database already exists.")


def add_score(name, difficulty):
    points_of_winning = (difficulty * 3) + 5
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT score FROM scores WHERE username = ?', (name,))
    row = cursor.fetchone()

    if row:
        new_score = row[0] + points_of_winning
        cursor.execute('UPDATE scores SET score = ? WHERE username = ?', (new_score, name))
    else:
        cursor.execute('INSERT INTO scores (username, score) VALUES (?, ?)', (name, points_of_winning))

    conn.commit()
    conn.close()


def get_scores():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username, score FROM scores')
    scores = cursor.fetchall()
    conn.close()
    return scores


@app.route('/', methods=['GET'])
def score_server():
    try:
        scores = get_scores()
        scores_html = ''.join(f"<li>{username}: {score}</li>" for username, score in scores)
        return f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The scores are:</h1>
        <ul>{scores_html}</ul>
    </body>
</html>
"""
    except Exception as e:
        return f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1><div id="score" style="color:red">{e}</div></h1>
    </body>
</html>
        """


def run_flask_app():
    app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    app.run(debug=True)
