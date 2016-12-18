import collections

def main():
    # Initialize sector ID total
    total = 0

    # Read in the rooms
    with open("InputDay04.txt") as f:
        inputStr = f.readlines()
    rooms = [room.split('-') for room in inputStr]

    # Check if each room is real
    for room in rooms:
        # Generate a letter count
        letterStr = "".join(room[:-1])
        letterCount = collections.Counter(letterStr)

        # Generate the checksum
        mc = sorted(letterCount.most_common(), key=lambda x: (-x[1], x[0]))
        s = "".join([l[0] for l in mc[:5]])

        # Retrieve the given checksum and sector ID
        checkSum = (room[-1].split(']')[0]).split('[')

        # If the checksums match, add the sector ID to the total
        if (s == checkSum[1]):
            total += int(checkSum[0])

            # Rotate name through the cipher
            rs = ""
            for l in letterStr:
                n = ord(l) + (int(checkSum[0]) % 26)
                if n > 122:
                    n -= 26
                rs += chr(n)

            # Print name if it is related to the north pole
            if ("northpole" in rs):
                print("Day04 Part2: " + str(checkSum[0]))

    # Print the sector ID total
    print("Day04 Part1: " + str(total))

if __name__ == "__main__":
    main()