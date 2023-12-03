dirs = [
    (1, 0), #right
    (-1, 0), #left
    (0, 1), #down
    (0, -1), #up
    (1, 1), #down-right
    (1, -1), #up-right
    (-1, -1), #up-left
    (-1, 1), #down-left
]

sum1 = 0
schematic = []
nums = {}
added = {}
f = open("Day3/input.txt")

def valid_pos(c, r):
    if c >= 0 and r >= 0:
        if c <= len(schematic[0]) and r <= len(schematic):
            return True
    return False

def check_dirs(r, c):
    sum = 0
    for d in dirs:
        nr = r + d[0]
        nc = c + d[1]
        if valid_pos(nr, nc):
            if ord(schematic[nr][nc]) >= 48 and ord(schematic[nr][nc]) <= 57:
                tc = nc
                while nums.get((str(nr) + "_" + str(tc)), -1) == -1:
                    tc += 1
                if added.get((str(nr) + "_" + str(tc)), -1) == -1:
                    sum += int(nums[str(nr) + "_" + str(tc)])
                    added[str(nr) + "_" + str(tc)] = True
                    print(f"Adding {int(nums[str(nr) + '_' + str(tc)])} to sum...")
    return sum


row = 0
for l in f:
    l = l.strip()
    col = 0
    line = []
    curr_num = ""
    for x in l:
        if (ord(x) >= 48 and ord(x) <= 57):
            curr_num += x
            if col == len(l) - 1:
                nums[str(row) + "_" + str(col)] = curr_num
        else:
            if curr_num:
                nums[str(row) + "_" + str(col - 1)] = curr_num
                curr_num = ""
        line.append(x)
        col += 1
    schematic.append(line)
    row += 1

for r in range(len(schematic)):
    for c in range(len(schematic[0])):
        if not (ord(schematic[r][c]) == 46 or (ord(schematic[r][c]) >= 48 and ord(schematic[r][c]) <= 57)):
            sum1 += check_dirs(r, c)
            print(f"Sum = {sum1}")

print(sum1)