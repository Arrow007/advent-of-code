# I need to take what's in the strategy guide, then basically calculate the score for every line. Then sum all of it together.
guide = open('../input.txt', mode='r')
lines = guide.readlines()

score = 0
lose = 0
draw = 3
win = 6
x = 1
y = 2
z = 3

for line in lines:
    opponent = line[0]
    player = line[2]

    match opponent:
        # Rock
        case 'A':
            match player:
                case 'X':
                    score += draw + x
                case 'Y':
                    score += win + y
                case 'Z':
                    score += lose + z

        # Paper
        case 'B':
            match player:
                case 'X':
                    score += lose + x
                case 'Y':
                    score += draw + y
                case 'Z':
                    score += win + z

        # Scissors
        case 'C':
            match player:
                case 'X':
                    score += win + x
                case 'Y':
                    score += lose + y
                case 'Z':
                    score += draw + z

print(score)

guide.close()