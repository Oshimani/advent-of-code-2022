opponent_chiffre = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
my_chiffre = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}

scores_by_pick = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
scores_by_outcome = {"win": 6, "loss": 0, "tie": 3}


def get_match_result(opponent, me):
    print(f"opponent: {opponent}, me: {me}")
    if opponent == me:
        return "tie"
    elif opponent == "ROCK":
        if me == "PAPER":
            return "win"
        else:
            return "loss"
    elif opponent == "PAPER":
        if me == "SCISSORS":
            return "win"
        else:
            return "loss"
    elif opponent == "SCISSORS":
        if me == "ROCK":
            return "win"
        else:
            return "loss"


def award_points(opponent, me):
    match_result = get_match_result(opponent_chiffre[opponent], my_chiffre[me])
    score = 0
    score += scores_by_pick[my_chiffre[me]]
    score += scores_by_outcome[match_result]
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
