f = open("Day2/input.txt")

sum = 0

for l in f:
    max_colors = {
        "red": -1,
        "green": -1,
        "blue": -1,
    }
    s = l[l.find(':') + 2:]
    games = s.split(';')
    for g in games:
        colors = g.split(',')
        for c in colors:
            nc = c.strip()
            pair = nc.split(' ')
            if "red" in pair[1] and int(pair[0]) > max_colors["red"]:
                max_colors["red"] = int(pair[0])
            if "green" in pair[1] and int(pair[0]) > max_colors["green"]:
                max_colors["green"] = int(pair[0])
            if "blue" in pair[1] and int(pair[0]) > max_colors["blue"]:
                max_colors["blue"] = int(pair[0])
    sum += (max_colors["red"] * max_colors["green"] * max_colors["blue"])
print(f"sum={sum}")
