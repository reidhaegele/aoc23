f = open("Day2/input.txt")

id = 1
sum = 0
valid = True

for l in f:
    s = l[l.find(':') + 2:]
    games = s.split(';')
    for g in games:
        colors = g.split(',')
        for c in colors:
            nc = c.strip()
            pair = nc.split(' ')
            if "red" in pair[1] and int(pair[0]) > 12:
                valid = False
                break
            if "green" in pair[1] and int(pair[0]) > 13:
                valid = False
                break
            if "blue" in pair[1] and int(pair[0]) > 14:
                valid = False
                break
    if not valid:
        valid = True
    else:
        sum += id
    id += 1
print(f"sum={sum}")
