from collections import Counter
from random import choice


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name):
        self.name = name
        self._rps_map = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

    def can_defeat(self, roll):
        return self._rps_map[self.name] == roll.name

    def is_tied_with(self, roll):
        return self.name == roll.name


def get_players_name():
    return input("player name: ").strip()


def get_players_roll():
    choice = input("\nroll ['rock', 'paper', 'scissors']: ").strip()
    return Roll(choice)


def build_the_three_rolls():
    rock = Roll("rock")
    paper = Roll("paper")
    scissors = Roll("scissors")
    return (rock, paper, scissors)


def print_header():
    print("-" * 50)
    print("Rock, Paper, Scissors".center(50))
    print("-" * 50)


def compute_winner(player1, player2, scores):
    if scores[player1.name] == scores[player2.name]:
        return "It's a tie"
    elif scores[player1.name] > scores[player2.name]:
        return f"{player1.name} wins!"
    else:
        return f"{player2.name} wins!"


def main():
    print_header()

    rolls = build_the_three_rolls()
    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    scores = Counter()
    scores[player1.name] = 0
    scores[player2.name] = 0

    count = 1
    while count < 3:
        print(f"\nROUND {count}:")
        p2_roll = choice(rolls)
        p1_roll = get_players_roll()

        # if both players roll the same, let's retry the round
        if p1_roll.is_tied_with(p2_roll):
            print(f"\nROUND {count} is a tie: {p1_roll.name}/{p2_roll.name}\n")
            continue

        player1_wins = p1_roll.can_defeat(p2_roll)

        # display throws
        print(f"{player1.name}: {p1_roll.name}\n" f"{player2.name}: {p2_roll.name}")

        # display winner for this round
        round_winner = player1.name if player1_wins else player2.name
        print(f"=> round {count} winner: {round_winner}")

        # record score
        scores[round_winner] += 1

        # increment round
        count += 1

    # Compute who won
    result = compute_winner(player1, player2, scores)
    print(
        f"\nResult: {result} "
        f"\n=> {player1.name}: {scores[player1.name]}"
        f"\n=> {player2.name}: {scores[player2.name]}"
    )


if __name__ == "__main__":
    main()
