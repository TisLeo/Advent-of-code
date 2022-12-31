# Get lines
lines = []
with open('../inputs/day4.txt', 'r') as f:
    lines = f.readlines()

# Split each line into 2 elves
# Get min and max of each elf
# Make array of min to max of each elf
# Check if elf1's array (of sections) is a subset of elf2's, and vice versa...
# ...Append result by 1 for each line if this is the case
def part1():
    result = 0
    
    for line in lines:
        line = line.replace("\n", '')
        elf1, elf2 = line.split(",")

        elf1_min, elf1_max = elf1.split("-")
        elf2_min, elf2_max = elf2.split("-")

        elf1_sections = []
        for i in range(int(elf1_min), int(elf1_max)+1):
            elf1_sections.append(i)

        elf2_sections = []
        for i in range(int(elf2_min), int(elf2_max)+1):
            elf2_sections.append(i)

        if (set(elf1_sections).issubset(set(elf2_sections))) or (set(elf2_sections).issubset(set(elf1_sections))):
            result += 1
     
    print("Result part 1:",result)


# Same as above, except...instead of checking if arrays are subsets of each other,
# check if any element in elf 1's array is included in elf 2's array (also works vice-versa).
# If this is the case, append result by 1
def part2():
    result = 0
    
    for line in lines:
        line = line.replace("\n", '')
        elf1, elf2 = line.split(",")

        elf1_min, elf1_max = elf1.split("-")
        elf2_min, elf2_max = elf2.split("-")

        elf1_sections = []
        for i in range(int(elf1_min), int(elf1_max)+1):
            elf1_sections.append(i)

        elf2_sections = []
        for i in range(int(elf2_min), int(elf2_max)+1):
            elf2_sections.append(i)
        
        flag = False
        for i in elf1_sections:
            if i in elf2_sections:
                flag = True
                break
        
        if flag:
            result += 1
    
    print("Result part 2", result)

part1()
part2()