f = open("Day4/input.txt")

total = 0

for l in f:
    curr = 0.5
    l = l[l.find(':') + 2:]
    l = l.replace('  ', ' ')
    both = l.split('|')
    winners = both[0].strip()
    his = both[1].strip()
    
    winners = winners.split(' ')
    his = his.split(' ')
    print(f"{winners} | {his}")
    for h in his:
        if h in winners:
           curr *= 2
           winners.remove(h)
    
    if curr >= 1:
        total += curr

print(total)
    