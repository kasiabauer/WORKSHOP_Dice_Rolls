from random import randint

POSSIBLE_DICES = ('D100', 'D20', 'D12', 'D10', 'D8', 'D6', 'D4', 'D3')


def roll_the_dice(dice_code):
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:  # splitting information from dice
                dice_split = dice_code.split(dice)
                multiply = dice_split[0]
                modifier = dice_split[1]

                try:
                    if multiply == "":  # assigning value if there is none for multiply
                        multiply = 1
                    else:
                        multiply = int(multiply)

                except ValueError:
                    return 'Wrong Input'

                try:
                    if modifier == "":  # assigning value if there is none for modifier
                        modifier = 0
                    else:
                        modifier = int(modifier)
                except ValueError:
                    return 'Wrong Input'

                dice_face = int(dice.split('D')[1])  # getting dice face and casting to int

                x = sum([randint(1, dice_face) for _ in range(multiply)]) + modifier  # rolling the dice and adding mod
                return x
            except ValueError:
                return 'Wrong Input'
    else:
        return 'Wrong Input'


print(roll_the_dice('2D12'))