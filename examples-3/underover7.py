import random
import re

def roll_dice(count, die):
    return [random.randint(1, die) for i in range(count)]

def roll_string(dice_description):
    match = re.match(r"(?P<count>[0-9]+)d(?P<die>[0-9]+)", dice_description)
    if not match:
        raise Exception(f"Invalid dice description {dice_description}")
    return roll_dice(int(match.groupdict()["count"]),
                int(match.groupdict()["die"]))

def game():
    bet = random.choice(["under 7", "7", "over 7"])
    roll = sum(roll_string("2d6"))
    if roll < 7 and bet == "under 7":
        return 1
    elif roll > 7 and bet == "over 7":
        return 1
    elif roll == 7 and bet == "7":
        return 3
    else:
        return -1

def session(trials=10000):
    winnings = 0
    for i in range(trials):
        winnings += game()
    print(f"Total winnings after {trials} games: {winnings}")

session()
