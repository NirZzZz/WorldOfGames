from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def score_server():
    try:
        with open("Scores.txt", "r") as file:
            content = file.read()
        return f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{content}</div></h1>
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
    <body>
        <h1><div id="score" style="color:red">{e}</div></h1>
    </body>
</html>
        """


if __name__ == '__main__':
    app.run(debug=True)
