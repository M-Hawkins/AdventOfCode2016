from __future__ import print_function

# Helper function for building bot properties from a set of instructions
def buildBots(stripInput):
    # Initialize an empty bots dictionary
    # Format will be: {botNum : [lowChip, highChip, lowDest, highDest]}
    bots = {}

    # For each instruction...
    for line in stripInput:
        instruction = line.split(' ')

        # If value instruction, initialize starting chip
        if instruction[0] == 'value':
            botNum = int(instruction[-1])
            newVal = int(instruction[1])

            # If the bot already exists, insert the new value appropriately
            if botNum in bots.keys():
                bot = bots[botNum]
                if bot[0] == -1:
                    bot[0] = newVal
                elif bot[0] < newVal:
                    bot[1] = newVal
                else:
                    bot[1] = bot[0]
                    bot[0] = newVal

            # Otherwise, create a new bot
            else:
                bots[botNum] = [newVal, -1, -1, -1]

        # If bot instruction, initialize destinations
        elif instruction[0] == "bot":
            botNum = int(instruction[1])

            # Use an int if the destination is a bot and a string if the 
            # destination is an output box
            if instruction[5] == "bot":
                lowDest = int(instruction[6])
            else:
                lowDest = instruction[6]
            if instruction[10] == "bot":
                highDest = int(instruction[11])
            else:
                highDest = int(instruction[11])

            # If the bot already exists, insert the destinations appropriately
            if botNum in bots.keys():
                bots[botNum][2] = lowDest
                bots[botNum][3] = highDest

            # Otherwise, create a new bot
            else:
                bots[botNum] = [-1, -1, lowDest, highDest]

    # Return the dictionary of bots
    return bots

# Helper function for having a bot distribute its chips
def giveChips(bots, botNum, botProps):
    lowChip, highChip, lowDest, highDest = botProps
    outChip = 1

    # If giving away the specified chip pair, print the current bot number
    if lowChip == 17 and highChip == 61:
        print("Day10 Part1: " + str(botNum))

    # If the destination is a bot, give that bot the chip
    if isinstance(lowDest, int):
        lowBot = bots[lowDest]
        if lowBot[0] == -1:
            lowBot[0] = lowChip
        elif lowBot[0] < lowChip:
            lowBot[1] = lowChip
        else:
            lowBot[1] = lowBot[0]
            lowBot[0] = lowChip

    # Otherwise, track the chip number if the output bin is 0, 1, or 2
    elif int(lowDest) > -1 and int(lowDest) < 3:
        outChip *= lowChip

    # If the destination is a bot, give that bot the chip
    if isinstance(highDest, int):
        highBot = bots[highDest]
        if highBot[0] == -1:
            highBot[0] = highChip
        elif highBot[0] < highChip:
            highBot[1] = highChip
        else:
            highBot[1] = highBot[0]
            highBot[0] = highChip

    # Otherwise, track the chip number if the output bin is 0, 1, or 2
    elif int(highDest) > -1 and int(highDest) < 3:
        outChip *= highChip

    # Remove both chips from the current bot
    bots[botNum][0] = -1
    bots[botNum][1] = -1

    # Return the modified bots dictionary and the output bin tracker
    return bots, outChip


# Main function
def main():
    # Read in the input
    with open("InputDay10.txt") as f:
        inputStr = f.readlines()
    stripInput = [line.strip() for line in inputStr]

    # Create a dictionary of bots with properties based on the instructions
    bots = buildBots(stripInput)

    # Intialize loop control out output bin tracker
    activeBot = True
    chipProd = 1

    # Loop until no bot gives away chip during an iteration of the loop
    while(activeBot):
        activeBot = False

        # Iterate through each bot...
        for botNum, botProps in bots.iteritems():
            # If the bot has two chips
            if botProps[0] != -1 and botProps[1] != -1:
                # Give away its chips
                bots, outChip = giveChips(bots, botNum, botProps)

                #Loop again and track output bin results
                activeBot = True
                chipProd *= outChip
                break

    # Print out the final product of the chip numbers in the first three bins
    print("Day10 Part2: " + str(chipProd))

if __name__ == "__main__":
    main()
