# Helper function for detecting ABBA support
def abba(ip):
    outsideBrackets = any(a == d and b == c and a != b
                          for a, b, c, d in zip(ip[0], ip[0][1:], ip[0][2:],
                                                ip[0][3:]))
    insideBrackets = any(a == d and b == c and a != b
                         for a, b, c, d in zip(ip[1], ip[1][1:], ip[1][2:],
                                               ip[1][3:]))
    return outsideBrackets and not insideBrackets

# Helper function for detecting ABA support
def aba(ip):
    return any(a == c and a != b and b+a+b in ip[1]
               for a, b, c in zip(ip[0], ip[0][1:], ip[0][2:]))

# Main function
def main():
    # Read in the input
    with open("InputDay7.txt") as f:
        inputStr = f.readlines()
    # Split the input and group it depending on whether the characters are
    # inside of outside of square brackets
    inputStrip = [w.strip() for w in inputStr]
    wordList = [line.replace('[', ']').split(']') for line in inputStrip]
    groupIP = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in wordList]

    # Print the number of ips with ABBA and ABA support
    print(sum(abba(ip) for ip in groupIP))
    print(sum(aba(ip) for ip in groupIP))

if __name__ == "__main__":
    main()
