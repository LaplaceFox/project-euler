from math import floor
from timeme import timeme

def eval_game(turns):
    # Returns probability of happening and win/loss
    # For each turn, 1 means blue and 0 means red

    prob = 1
    disks = 2 # number of disks
    for i in range(len(turns)):
        if turns[i]: # if we pull blue
            prob *= 1/(disks+i)
        else: # if we pull red
            prob *= 1 - 1/(disks+i)
    
    # Check if #blue > #red
    is_win = (sum(turns) > (len(turns) - sum(turns)))

    return (prob,is_win)

def solution():
    win_prob = 0
    for i in range(2**15):
        turnstr = "{:0>15b}".format(i)
        turns = [int(t) for t in turnstr]

        (p,w) = eval_game(turns)
        if w:
            win_prob += p
        
    return floor(1/win_prob)

timeme(solution)