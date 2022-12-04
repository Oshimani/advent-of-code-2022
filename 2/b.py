opponent_chiffre = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
outcome_chiffre = {"X": "loss", "Y": "tie", "Z": "win"}

scores_by_pick = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
scores_by_outcome = {"win": 6, "loss": 0, "tie": 3}

def get_my_pick(opponent:str, outcome:str):
    if opponent == "ROCK":
        if outcome == "win":
            return "PAPER"
        if outcome == "loss":
            return "SCISSORS"
        return "ROCK"
    if opponent == "PAPER":
        if outcome == "win":
            return "SCISSORS"
        if outcome == "loss":
            return "ROCK"
        return "PAPER"
    if opponent == "SCISSORS":
        if outcome == "win":
            return "ROCK"
        if outcome == "loss":
            return "PAPER"
        return "SCISSORS"

def award_points(opponent, outcome):
    my_pick = get_my_pick(opponent_chiffre[opponent], outcome_chiffre[outcome])
    score = 0
    score += scores_by_pick[my_pick]
    score += scores_by_outcome[outcome_chiffre[outcome]]
    return score


with open("./2/input.txt", "r") as f:
    lines = f.readlines()

    my_score = 0
    for line in lines:
        if line == "\n":
            continue
        line = line[:-1]
        print(line)
        points = award_points(line[0], line[2])
        print(points)
        my_score += points
    print(f"Total score: {my_score}")
