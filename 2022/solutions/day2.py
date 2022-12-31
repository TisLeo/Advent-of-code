# Define points
rock = 1
paper = 2
scissors = 3
draw = 3
win = 6

#Get lines
lines = []
with open("../inputs/day2.txt", 'r') as f:
    lines = f.readlines()

# Separate each round
# Match to losing, drawing or winning combos
# Hence determine points
# Add pts for each round into a total
def part1():
    losing_combos = ["A Z", "B X", "C Y"]
    drawing_combos = ["A X", "B Y", "C Z"]

    total = 0
    for i in lines:
        i = i.replace('\n', '')
        round_total = 0
        current_round = str(i)
        my_go = current_round[2]
        if current_round in losing_combos:
            match my_go:
                case 'X':
                    round_total += rock
                case 'Y':
                    round_total += paper
                case 'Z':
                    round_total += scissors
        elif current_round in drawing_combos:
            match my_go:
                case 'X':
                    round_total += draw + rock
                case 'Y':
                    round_total += draw + paper
                case 'Z':
                    round_total += draw + scissors
        else: # must be winning combo
            match my_go:
                case 'X':
                    round_total += win + rock
                case 'Y':
                    round_total += win + paper
                case 'Z':
                    round_total += win + scissors
        
        total += round_total

    print("Total points part 1:", total) # ANSWER

# Separate each round
# Match whether i need to lose, draw or win with opponent's go
# Hence determine points and add to total
def part2():
    total = 0
    for i in lines:
        i = i.replace('\n', '')
        round_total = 0
        current_round = str(i)
        opponent_go = str(current_round[0])
        my_go = current_round[2]

        match my_go:
            case 'X': # I need to lose
                match opponent_go:
                    case 'A':
                        round_total += scissors
                    case 'B':
                        round_total += rock
                    case 'C':
                        round_total += paper
            case 'Y': # I need to draw
                match opponent_go:
                    case 'A':
                        round_total += draw + rock
                    case 'B':
                        round_total += draw + paper
                    case 'C':
                        round_total += draw + scissors
            case 'Z': # I need to win
                match opponent_go:
                    case 'A':
                        round_total += win + paper
                    case 'B':
                        round_total += win + scissors
                    case 'C':
                        round_total += win + rock 

        total += round_total
    
    print("Total points part 2:", total)

part1()
part2()