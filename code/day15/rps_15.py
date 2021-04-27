import csv
from collections import Counter
from pathlib import Path
from random import choice

BATTLE_CARD_FILE = "battle-table.csv"


class BattleCard:
    def __init__(self, mapping: dict = None):
        self.mapping = mapping

    @property
    def attackers(self):
        if self.mapping:
            return [x for x in self.mapping]
        return []

    def from_csv(self, filename):
        with Path(filename).open() as csvfile:
            reader = csv.DictReader(csvfile)
            battle_dict = {}
            for row in reader:
                attacker = row.pop("Attacker")
                battle_dict[attacker] = row
            self.mapping = battle_dict


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name):
        self.name = name
        self.battle_card = None

    def set_battle_card(self, battle_card):
        self.battle_card = battle_card

    def can_defeat(self, roll):
        return self.battle_card.mapping[self.name] == roll.name

    def is_tied_with(self, roll):
        return self.name == roll.name


def get_players_name():
    return input("player name: ").strip()


def get_players_roll(battlecard):
    print(f"Choices: {', '.join(battlecard.attackers)}")
    choice = input("\nroll: ").strip()
    roll = Roll(choice)
    roll.set_battle_card(battlecard)
    return roll


def build_rolls(battle_card):
    return [Roll(attacker) for attacker in battle_card.attackers]


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

    battle_card = BattleCard()
    battle_card.from_csv(BATTLE_CARD_FILE)

    rolls = build_rolls(battle_card)
    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls, battle_card)


def game_loop(player1, player2, rolls, battle_card):
    scores = Counter()
    scores[player1.name] = 0
    scores[player2.name] = 0

    count = 1
    while count < 3:
        print(f"\nROUND {count}:")
        p2_roll = choice(rolls)
        p2_roll.set_battle_card(battle_card)
        p1_roll = get_players_roll(battle_card)

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
