def main():
    # Initialize keypad and finger location
    keys = [['*', '*', '1', '*', '*'],
            ['*', '2', '3', '4', '*'],
            ['5', '6', '7', '8', '9'],
            ['*', 'A', 'B', 'C', '*'],
            ['*', '*', 'D', '*', '*']]
    loc = [0, 2]
    code = ""

    # Read in the commands
    with open("InputDay2.txt") as f:
        inputStr = f.readlines()
        inputStr = [s.strip() for s in inputStr]

    # Iterate through each button press
    for commands in inputStr:
        # Iterate through each command
        for command in commands:
            if command == 'U':
                loc[1] = max(abs(2 - loc[0]), loc[1] - 1)
            elif command == 'D':
                loc[1] = min(4 - abs(2 - loc[0]), loc[1] + 1)
            elif command == 'L':
                loc[0] = max(abs(2 - loc[1]), loc[0] - 1)
            elif command == 'R':
                loc[0] = min(4 - abs(2 - loc[1]), loc[0] + 1)
        # Add the button press to the code
        code += keys[loc[1]][loc[0]]

    # Print out the key code
    print(code)

if __name__ == "__main__":
    main()