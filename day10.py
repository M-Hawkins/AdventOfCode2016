from __future__ import print_function

def buildBots(stripInput):
    bots = {}

    #{botNum : [lowChip, highChip, lowDest, highDest]}
    for line in stripInput:
        instruction = line.split(' ')
        if instruction[0] == 'value':
            botNum = int(instruction[-1])
            newVal = int(instruction[1])
            if botNum in bots.keys():
                bot = bots[botNum]
                if bot[0] == -1:
                    bot[0] = newVal
                elif bot[0] < newVal:
                    bot[1] = newVal
                else:
                    bot[1] = bot[0]
                    bot[0] = newVal
            else:
                bots[botNum] = [newVal, -1, -1, -1]
        elif instruction[0] == "bot":
            #bot 2 gives low to bot 1 and high to bot 0
            botNum = int(instruction[1])
            lowType = instruction[5]
            lowDest = int(instruction[6])
            highType = instruction[10]
            highDest = int(instruction[11])

            if botNum in bots.keys():
                bot = bots[botNum]
                if lowType == "bot":
                    bot[2] = lowDest
                if highType == "bot":
                    bot[3] = highDest
            else:
                if lowType == "bot" and highType == "bot":
                    bots[botNum] = [-1, -1, lowDest, highDest]
                elif lowType == "bot":
                    bots[botNum] = [-1, -1, lowDest, -1]
                elif highType == "bot":
                    bots[botNum] = [-1, -1, -1, highDest]
                else:
                    bots[botNum] = [-1, -1, -1, -1]
    return bots

def giveChips(bots, botNum, botProps):
    lowChip, highChip, lowDest, highDest = botProps

    # print(str(botNum) + ": " + str(lowDest) + ": " + str(lowChip) + ", " + str(highDest) + ": " + str(highChip))
    if lowChip == 17 and highChip == 61:
        print("FOUND: " + str(botNum))

    if lowDest != -1:
        lowBot = bots[lowDest]
        if lowBot[0] == -1:
            lowBot[0] = lowChip
        elif lowBot[0] < lowChip:
            lowBot[1] = lowChip
        else:
            lowBot[1] = lowBot[0]
            lowBot[0] = lowChip
    if highDest != -1:
        highBot = bots[highDest]
        if highBot[0] == -1:
            highBot[0] = highChip
        elif highBot[0] < highChip:
            highBot[1] = highChip
        else:
            highBot[1] = highBot[0]
            highBot[0] = highChip

    bots[botNum][0] = -1
    bots[botNum][1] = -1

    return bots


# Main function
def main():
    # Read in the input
    with open("InputDay10.txt") as f:
        inputStr = f.readlines()
    stripInput = [line.strip() for line in inputStr]

    bots = buildBots(stripInput)

    activeBot = True
    while(activeBot):
        activeBot = False
        for botNum, botProps in bots.iteritems():
            if botProps[0] != -1 and botProps[1] != -1:
                bots = giveChips(bots, botNum, botProps)
                activeBot = True
                break

    # print()
    # for botNum, botProps in bots.iteritems():
    #     print(str(botNum) + ": " + str(botProps))
        

if __name__ == "__main__":
    main()
