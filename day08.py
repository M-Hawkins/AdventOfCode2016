from __future__ import print_function

# Helper function for printing out the screen
def gridPrint(screen):
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            print(screen[y][x], end=" ")
        print()
    print()

# Helper function for counting the number of lit pixels
def gridCount(screen):
    cnt = 0
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] == "#":
                cnt += 1
    return cnt

# Main function
def main():
    # Read in the input
    with open("InputDay08.txt") as f:
        inputStr = f.readlines()
    stripInput = [line.strip() for line in inputStr]

    # Initialize the screen
    screen =[[' '] * 50 for _ in range(6)]

    # Iterate through each instruction
    for instruction in stripInput:
        i = instruction.split(' ')
        # rect instruction case
        if i[0] == "rect":
            # Get the diminsions and light up the grid
            c = i[1].split('x')
            for y in range(int(c[1])):
                for x in range(int(c[0])):
                    screen[y][x] = '#'

        # row case
        elif i[0] == "rotate" and i[1] == "row":
            # Get the index and amount
            y = int(i[2].split('=')[1])
            amt = int(i[4])
            endSlice = len(screen[y]) - amt

            # Shift the given row by the given amount
            screen[y] = screen[y][endSlice:] + screen[y][:endSlice]

        # column case
        elif i[0] == "rotate" and i[1] == "column":
            # Get the index and amount
            x = int(i[2].split('=')[1])
            amt = int(i[4])
            endSlice = len(screen) - amt

            # Build a column vector
            ele = [screen[y][x] for y in range(len(screen))]

            # Shift the column vector by the given amount
            ele = ele[endSlice:] + ele[:endSlice]

            # Overwrite the column with the values in the shifted column vector
            for y in range(len(screen)):
                screen[y][x] = ele[y]

        # print(instruction)
        # gridPrint(screen)
        # print('----------')

    # Print out the screen and the number of lit pixels
    gridPrint(screen)
    print(gridCount(screen))

if __name__ == "__main__":
    main()
