# Get lines
lines = []
with open('../inputs/day3.txt', 'r') as f:
    lines = f.readlines()

# Split each line into 2
# Find common character
# Get priority of common character using ASCII values
# Add priorities of each common char
def part1():
    total = 0

    for i in lines:
        i = i.replace("\n", '')
        first, second = i[:len(i)//2], i[len(i)//2:]

        common_char = ''
        for c in first:
            if c in second:
                common_char = c

        priority = 0
        if common_char.isupper():
            priority = (ord(common_char) - 65) + 27
        else:
            priority = (ord(common_char) - 96)
        
        total += priority

    print("Total part 1:", total)

# Group every other 3 lines
# Find common character (the badge)
# Find priority of badge in each group
# Add priorities
def part2():
    total = 0
    i = 0

    while i <= len(lines)-3:
        group = lines[i:i+3]
        for j in range(0, len(group)):
            group[j] = group[j].replace("\n", '')

        badge = ''
        for c in group[0]:
            if c in group[1] and c in group[2]:
                badge = c

        priority = 0
        if badge.isupper():
            priority = (ord(badge) - 65) + 27
        else:
            priority = (ord(badge) - 96)
        
        total += priority
        i += 3

    print("Total part 2:", total) # ANSWER

part1()
part2()