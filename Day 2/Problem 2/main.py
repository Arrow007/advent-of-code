# I need to take what's in the strategy guide, then basically calculate the score for every line. Then sum all of it together.
guide = open('../input.txt', mode='r')
lines = guide.readlines()

score = 0
loseX = 0
drawY = 3
winZ = 6
a = 1
b = 2
c = 3

for line in lines:
    opponent = line[0]
    outcome = line[2]

    match opponent:
        # Rock
        case 'A':
            match outcome:
                case 'X':
                    score += loseX + c
                case 'Y':
                    score += drawY + a
                case 'Z':
                    score += winZ + b

        # Paper
        case 'B':
            match outcome:
                case 'X':
                    score += loseX + a
                case 'Y':
                    score += drawY + b
                case 'Z':
                    score += winZ + c

        # Scissors
        case 'C':
            match outcome:
                case 'X':
                    score += loseX + b
                case 'Y':
                    score += drawY + c
                case 'Z':
                    score += winZ + a

print(score)

guide.close()