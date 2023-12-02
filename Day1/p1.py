f = open("Day1\input.txt")
first = -1
last = -1
sum = 0

for l in f:    
    for x in l:
        if ord(x) >= 49 and ord(x) <= 57:
            if first == -1:
                first = int(x)
            else:
                last = int(x)
    if last == -1:
        last = first
    print(f"{first}{last}")
    sum += ((first * 10) + last)
    print(f"Sum: {sum}")
    first = -1
    last = -1
        