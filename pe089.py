from timeme import timeme

roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def get_value(r):
    nums = list(map(lambda x: roman[x], list(r)))

    acc = 0
    while len(nums) > 1:
        cur = nums.pop(0)
        if cur < nums[0]:
            nums[0] -= cur
        else:
            acc += cur
    return acc + nums[0]

def roman_length(n):
    numstr = str(n).rjust(4,"0")
    total = int(numstr[0]) # leave thousands place untouched

    #For the rest of the digits
    for d in str(n).rjust(4,"0")[1:]:
        dig = int(d)
        if dig in [4,9]: #uses IX, XC, XM
            total += 2
        elif dig <= 3:
            total += dig
        else:
            total += dig - 4
    return total

def solution():
    total = 0
    f = open("p089_roman.txt")
    for line in f.readlines():
        line = line.strip()
        total += len(line) - roman_length(get_value(line))
    return total

timeme(solution)