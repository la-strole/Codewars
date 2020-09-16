def score(dice):
    dice_copy = dice[:]
    variants = [1, 6, 5, 4, 3, 2]
    result = 0
    for item in variants:
        if dice_copy.count(item) >= 3:
            if item == 1:
                result += 1000
            else:
                result += item * 100
    result += 100 * (dice_copy.count(1) % 3)
    result += 50 * (dice_copy.count(5) % 3)
    return result

print (score([2, 4, 4, 5, 4]))