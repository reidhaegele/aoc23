with open("Day4/input.txt") as f:

    total = 0

    multi = {}
    index = 1
    lindex = 1
    for l1 in f:
        multi[lindex] = 1
        lindex+=1

    f.seek(0)
    
    for l in f:
        curr = 0
        l = l[l.find(':') + 2:]
        l = l.replace('  ', ' ')
        both = l.split('|')
        winners = both[0].strip()
        his = both[1].strip()
        
        winners = winners.split(' ')
        his = his.split(' ')
        # print(f"{winners} | {his}")
        for h in his:
            if h in winners:
                curr += 1
                winners.remove(h)
        
        
        index += 1
        # print(f"--------------------\nindex={index}; curr={curr}; \n{multi}")
        if curr >= 1:
            for j in range(multi[index-1]):
                for i in range(curr):
                    # if index == 5:
                        # print(f"i={i};j={j}")
                    multi[index + i] = multi[index + i] + 1
        # print(f"AFTER:\n{multi}\n---------------------------")

    # print(multi)
    print(sum(multi.values()))