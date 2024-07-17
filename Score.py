def add_score(_name, _difficulty):
    points_of_winning = (_difficulty * 3) + 5
    scores = {}
    try:
        with open("Scores.txt", "r") as file:
            for line in file:
                user, score = line.strip().split(':')
                scores[user] = int(score)
    except FileNotFoundError:
        pass

    if _name in scores:
        scores[_name] += points_of_winning
    else:
        scores[_name] = points_of_winning

    with open("Scores.txt", "w") as file:
        for user, score in scores.items():
            file.write(f"{user}:{score}\n")
