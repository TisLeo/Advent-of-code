# Get lines
lines = 0
with open('../inputs/day1.txt', 'r') as f:
    lines = f.readlines()

# Separate elves
# Add amount of calories per elf
# Get elf with largest amount
calories = []
def part1():
    temp = 0
    for i in lines:
        i = i.replace("\n", '')
        if any(char.isdigit() for char in i):
            temp += int(i)
        else:
            temp = 0

        if temp != 0:
            calories.append(temp)

    print("Elf with most calories:", max(calories)) # ANSWER

# Get max of calories array
# Remove max
# Repeat 3 times to get top 3
# Add calories of top 3 elves
def part2():
    top3 = []
    for i in range(0, 3):
        top3.append(max(calories))
        calories.remove(max(calories))

    total = 0
    for i in top3:
        total += i

    print("Total of top 3 elves with most calories:", str(total)) # ANSWER

part1()
part2()