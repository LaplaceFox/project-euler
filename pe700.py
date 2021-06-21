inc = 1504170715041707
md  = 4503599627370517

total = 1504170715041707
mn = total

current = total

while mn > 0:
    current = (current + inc) % md
    if current < mn:
        total += current
        print(mn)
        mn = current

print(total)