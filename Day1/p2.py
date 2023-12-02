f = open("Day1\input.txt")
first = -1
last = -1
sum = 0

digits = {
    "one": 1,
    "1":1,
    "two": 2,
    "2":2,
    "three": 3,
    "3":3,
    "four": 4,
    "4":4,
    "five": 5,
    "5":5,
    "six": 6,
    "6":6,
    "seven": 7,
    "7":7,
    "eight": 8,
    "8":8,
    "nine": 9,
    "9":9,
}

sizes = {
    "o":[3],
    "t":[3, 5],
    "f":[4, 4],
    "s":[3, 5],
    "e":[5],
    "n":[4],
}

for l in f:
    for i in range(len(l)):
        dig = digits.get(l[i], -1)
        if dig != -1:
            if first == -1:
                first = dig
            else:
                last = dig
        else:
            siz = sizes.get(l[i], -1)
            if siz != -1:
                for x in siz:
                    word = digits.get(l[i:i+x], -1)
                    if word != -1:
                        if first == -1:
                            first = word
                        else:
                            last = word
    if last == -1:
        last = first
    # print(f"{first}{last}")
    sum += ((first * 10) + last)
    # print(f"Sum: {sum}")
    first = -1
    last = -1
print(sum)