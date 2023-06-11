from itertools import product
from timeme import timeme

def dice_sums(num,sides):
    # Number of outcomes for each possible sum
    outcomes = product(range(1,sides+1),repeat=num)
    sums = list(map(sum, outcomes))
    return {x: sums.count(x) for x in range(num, num*sides + 1)}

def solution():
    pyramid = dice_sums(9,4)
    cube = dice_sums(6,6)

    total_pyramid = 4**9
    total_cube = 6**6

    win_prob = 0

    less_than_i = cube[6] + cube[7] + cube[8]
    for i in range(9,37): # Iterate over every possible 9d4 result
        win_prob += (pyramid[i]/total_pyramid) * (less_than_i/total_cube)
        less_than_i += cube[i] # Update for next iteration

    return win_prob

timeme(solution)