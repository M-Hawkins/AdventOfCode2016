def main():
    # Initialize starting location and direction
    xy = [0, 0]
    facing = [0, 1]
    visited = [[0, 0]]
    hq = -1

    # Read in input file and split by commas
    with open("InputDay1.txt") as f:
        inputStr = f.read()
        inputStr = inputStr.replace(' ', '')
    directions = inputStr.split(",")

    # Iterate through each command
    for d in directions:
        # Change the direction we are facing
        if d[0] == 'R':
            facing = [facing[1], -1 * facing[0]]
        else:
            facing = [-1 * facing[1], facing[0]]

        # Calculate how far we must walk
        amount = int(d[1:])

        # Walk the given number of blocks
        for step in range(amount):
            xy[0] += facing[0]
            xy[1] += facing[1]

            # Check if we have already visited this location
            if hq == -1:
                if xy not in visited:
                    visited.append(xy[:])
                else:
                    hq = xy[:]
    
    # Print how many blocks away we are total
    print(abs(xy[0]) + abs(xy[1]))
    
    # Print how many blocks away we are from the HQ
    print(abs(hq[0]) + abs(hq[1]))


if __name__ == "__main__":
    main()