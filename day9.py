from __future__ import print_function

# Main function
def main():
    # Read in the input
    with open("InputDay9.txt") as f:
        inputStr = f.read()
    stripInput = "".join(inputStr.split())

    splitInput = stripInput.replace("(", "*(")
    splitInput = splitInput.replace(")", ")*")
    splitInput = splitInput.split("*")
    splitInput = [x for x in splitInput if x]

    ans = ""

    for i in range(len(splitInput)):
        if splitInput[i] != "" and splitInput[i][0] == "(":
            dims = splitInput[i].split('x')
            numChars = int(dims[0][1:])
            numReps = int(dims[1][:-1])
            s = ""
            j = 1
            while len(s) < numChars:
                t = splitInput[i+j]
                t = t[:numChars-len(s)]
                s += t
                splitInput[i+j] = splitInput[i+j][len(t):]
                j += 1
            ans += s * numReps

        else:
            ans += splitInput[i]

    # print(ans)
    print(len(ans))

if __name__ == "__main__":
    main()
