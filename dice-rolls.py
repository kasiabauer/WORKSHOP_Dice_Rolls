from random import randint


# def dice_roll(number:int, face:int, mod=+10):
#     number_of_rolls = list(range(number))
#     roll_1 = 0
#
#     for roll in number_of_rolls:
#         rolls_result = 0
#         roll_1 = randint(1,face)
#         print(roll_1)
#         rolls_result += roll_1
#         print(rolls_result)
#     return rolls_result + mod
#
# print(dice_roll(2, 6))
# # print(dice_roll(2, d, 10, +10))

try:
    dice_info = input('Give dice info (example: 2D10+10): ')
    # if 'd' or 'D' not in dice_info:
    #     print("You need to use 'D' in the dice info")
except TypeError:
    print('Wrong input. Example: 2D10+10')

print(f'Rolling for: {dice_info}')

def split_dice_info(dice_info):
    dice_info_split = dice_info.split('D')
    dice_rolls = dice_info_split[0]
    dice_face = dice_info_split[1].split('+')[0]
    dice_mod = dice_info_split[1].split('+')[1]
    return dice_rolls, dice_face, dice_mod


# print(get_dice_info(2D10+20'))
dice_rolls = int(split_dice_info(dice_info)[0])
dice_face = int(split_dice_info(dice_info)[1])
dice_mod = int(split_dice_info(dice_info)[2])

def dx_roll(dice_rolls, dice_face, dice_mod):
    rnd_roll = randint(1, dice_face)
    print('rnd roll:', {rnd_roll})
    return sum([rnd_roll + dice_mod for _ in range(dice_rolls)])

print(dx_roll(dice_rolls, dice_face, dice_mod))
