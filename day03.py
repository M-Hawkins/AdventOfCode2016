def main():
    # Initialize count of correct triangles
    count = 0

    # Read in the commands
    with open("InputDay03.txt") as f:
        inputStr = f.readlines()
        splitLines = [line.split(' ') for line in inputStr]
        parsed = []
        for line in splitLines:
            line = [int(x.strip()) for x in line if x]
            parsed.append(line)

    #Iterate through the parsed set, incrementing by three
    for i in range(0, len(parsed) - 2, 3):
        # Iterate through the three colomns
        for j in range(3):
            # If it is a correct triangle, increment the counter
            if (parsed[i][j] + parsed[i+1][j] > parsed[i+2][j] and
                parsed[i][j] + parsed[i+2][j] > parsed[i+1][j] and
                parsed[i+1][j] + parsed[i+2][j] > parsed[i][j]):
                count += 1

    # Print out the total count
    print(count)

if __name__ == "__main__":
    main()