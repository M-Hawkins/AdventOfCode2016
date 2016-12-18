from __future__ import print_function

# Solution for part 1 which builds the decompressed string
def part1(stripInput):
    # Split the input so the marks and blocks of normal characters are separate
    splitInput = stripInput.replace("(", "*(")
    splitInput = splitInput.replace(")", ")*")
    splitInput = splitInput.split("*")
    splitInput = [x for x in splitInput if x]

    # Initialize an empty decompressed string
    ans = ""

    # For each mark or block of normal characters...
    for i in range(len(splitInput)):
        # If it's a mark..
        if splitInput[i] != "" and splitInput[i][0] == "(":
            # Extract the number of characters and repetitions indicated
            dims = splitInput[i].split('x')
            numChars = int(dims[0][1:])
            numReps = int(dims[1][:-1])

            # Initialize an empty substring
            s = ""
            j = 1

            # Grab numChars characters from future sections
            while len(s) < numChars:
                t = splitInput[i+j]
                t = t[:numChars-len(s)]
                s += t
                splitInput[i+j] = splitInput[i+j][len(t):]
                j += 1
            
            # Repeat the substring numReps times and add it to the decompressed
            ans += s * numReps

        # Otherwise, just add the normal characters to the string
        else:
            ans += splitInput[i]

    # Return the length of the decompressed string
    return len(ans)

# Recursive solution for part 2
def part2(stripInput):
    # Find the first mark
    pIndex = stripInput.find('(')

    # If there is none, return the number of normal characters
    if pIndex == -1:
        return len(stripInput)
    # Otherwise...
    else:
        # Extract the number of characters and repetitions indicated
        eIndex = stripInput.find(')')
        mark = stripInput[pIndex+1:eIndex].split('x')
        numChars = int(mark[0])
        numReps = int(mark[1])

        # Initialize the answer to the number of leading normal characters
        ans = len(stripInput[:pIndex])

        # Add the decompressed length of the marked substring times numReps
        lenRepStr = part2(stripInput[eIndex+1:eIndex+1+numChars])
        ans += numReps * lenRepStr

        # Add the decompressed length of the trailing substring
        ans += part2(stripInput[eIndex+1+numChars:])

        return ans

# Main function
def main():
    # Read in the input
    with open("InputDay09.txt") as f:
        inputStr = f.read()
    stripInput = "".join(inputStr.split())

    # Print out the answers for part 1 and 2
    print("Day09 Part1: " + str(part1(stripInput)))
    print("Day09 Part2: " + str(part2(stripInput)))

if __name__ == "__main__":
    main()
