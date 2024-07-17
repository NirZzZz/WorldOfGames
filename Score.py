def add_score(_difficulty):
    points_of_winning = (_difficulty * 3) + 5
    try:
        with open("Scores.txt", "r+") as file:
            content = file.read().strip()
            if content:
                last_score = content
                total = int(last_score) + int(points_of_winning)
                file.seek(0)
                file.write(str(total))
            else:
                file.write(str(points_of_winning))
    except FileNotFoundError:
        with open("Scores.txt", "w") as f:
            f.write(str(points_of_winning))
